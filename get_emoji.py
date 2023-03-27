from os.path import exists
from os import makedirs
import getBili


# 先从charge判断
def get_charge(uid, base_dir='./'):
    """
    输入:
        - uid: 目标用户mid
        - base_dir: 保存路径

    输出: 素材文件夹
    """

    charge_emoji = getBili.charge_emoji(uid)

    charge = charge_emoji.json()

    room_id, user_name = getBili.user_info(uid)

    live_emoji = getBili.live_emoji(room_id)

    room = live_emoji.json()

    base_dir += user_name + '表情'

    # 获取失败则不执行
    if room['code'] != 0:
        print('获取失败，房间专属表情' + room['message'])
        return
    else:
        if not exists(base_dir):
            makedirs(base_dir)
        # Save suit json if not exists
        if not exists(base_dir + '/' + 'room.json'):
            with open(base_dir + '/' + 'room.json', 'w',
                      encoding='utf-8') as room_json_file:
                room_json_file.write(live_emoji.text)
        # 判断[1]是否为room表情
        if room['data']['data'][1]['pkg_name'] == '房间专属表情':
            room_emoji_list = [
                (item['emoji'], item['url'])
                for item in room['data']['data'][1]['emoticons']
            ]

            getBili.download_emoji(room_emoji_list, base_dir)
        # 判断[2]是否为room表情
        elif room['data']['data'][2]['pkg_name'] == '房间专属表情':
            room_emoji_list = [
                (item['emoji'], item['url'])
                for item in room['data']['data'][2]['emoticons']
            ]

            getBili.download_emoji(room_emoji_list, base_dir)

    # 获取失败则不执行
    if charge['code'] != 0:
        print(charge['message'])
        return
    # 表情为空则不执行
    elif str(charge['data']['list']) == "[]":
        print('没有充电表情和UP主大表情')
        return
    else:
        if not exists(base_dir):
            makedirs(base_dir)
        # Save suit json if not exists
        if not exists(base_dir + '/' + charge['data']['list'][0]['panel_desc'] + '.json'):
            with open(base_dir + '/' + charge['data']['list'][0]['panel_desc'] + '.json', 'w',
                      encoding='utf-8') as emoji_json_file:
                emoji_json_file.write(charge_emoji.text)

        charge_emoji_list = [
            (item['text'][1:-1], item['url'])
            for item in charge['data']['list'][0]['emote']
        ]

        getBili.download_emoji(charge_emoji_list, base_dir)

        if charge['data']['list'][1] in charge['data']['list']:
            up_emoji_list = [
                (item['text'][1:-1], item['url'])
                for item in charge['data']['list'][1]['emote']
            ]

            getBili.download_emoji(up_emoji_list, base_dir)


while True:
    mid = eval(input("input UID: ").strip())
    get_charge(mid)
