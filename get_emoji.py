from os.path import exists
from os import makedirs
from json import dumps, loads
import errors
import getBili


def get_emoji(room_id, base_dir='./'):
    """
    输入:
        - room_id: room id
        - base_dir: 保存路径

    输出: 素材文件夹

    测试数据: 22967698
    """

    live_emoji = getBili.live_emoji(room_id)

    res = live_emoji.json()

    # emoji存在才执行
    if res['code'] != 0:
        errors._show_error(0)
        return dict(), 0
    else:
        base_dir += getBili.liver_name(getBili.liver_uid(room_id)) + '_表情'

        if not exists(base_dir):
            makedirs(base_dir)

        # Save suit json if not exists
        if not exists(base_dir + '/live_info.json'):
            with open(base_dir + '/live_info.json', 'w', encoding='utf-8') as suit_json_file:
                suit_json_file.write(live_emoji.text)

        if res['data']['data'][1]['pkg_name'] == 'UP主大表情':
            up_emoji_list1 = [
                (item['emoji'], item['url'])
                for item in res['data']['data'][1]['emoticons']
            ]
            getBili.download_emoji(up_emoji_list1, base_dir, 'UP_')
            if res['data']['data'][2]['pkg_name'] == '房间专属表情':
                up_emoji_list2 = [
                    (item['emoji'], item['url'])
                    for item in res['data']['data'][2]['emoticons']
                ]
                getBili.download_emoji(up_emoji_list2, base_dir)
        elif res['data']['data'][1]['pkg_name'] == '房间专属表情':
            up_emoji_list1 = [
                (item['emoji'], item['url'])
                for item in res['data']['data'][1]['emoticons']
            ]
            getBili.download_emoji(up_emoji_list1, base_dir)
            
