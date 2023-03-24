from os.path import exists
from os import makedirs
import errors
import getBili


def get_charge(uid, base_dir='./'):
    """
    输入:
        - room_id: room id
        - base_dir: 保存路径

    输出: 素材文件夹

    测试数据: 22967698
    """

    charge_emoji = getBili.charge_emoji(uid)

    res = charge_emoji.json()

    # 获取失败则不执行
    if res['code'] != 0:
        errors._show_error(0)
        print(res['message'])
        return dict(), 0
    # 表情为空则不执行
    elif str(res['data']['list']) == "[]":
        print('没有表情')
    else:
        dir1 = base_dir + res['data']['list'][0]['panel_desc']

        if not exists(dir1):
            makedirs(dir1)

        # Save suit json if not exists
        if not exists(base_dir + '/' + res['data']['list'][0]['panel_desc'] + '.json'):
            with open(base_dir + '/' + res['data']['list'][0]['panel_desc'] + '.json', 'w',
                      encoding='utf-8') as suit_json_file:
                suit_json_file.write(charge_emoji.text)

        up_emoji_list1 = [
            (item['text'][1:-1], item['url'])
            for item in res['data']['list'][0]['emote']
        ]

        getBili.download_emoji(up_emoji_list1, dir1)

        if res['data']['list'][1] in res['data']['list']:
            dir2 = base_dir + res['data']['list'][1]['panel_desc']

            if not exists(dir2):
                makedirs(dir2)

            up_emoji_list2 = [
                (item['text'][1:-1], item['url'])
                for item in res['data']['list'][1]['emote']
            ]

            getBili.download_emoji(up_emoji_list2, dir2)
