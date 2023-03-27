import requests

cookies = "_uid=your _uid; SESSDATA=your SESSDATA"

hd = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 '
                  'Safari/537.36 Edg/108.0.1462.54',
    'referer': 'https://www.bilibili.com',
    'Content-Type': 'application/json'
}

r = requests.Session()
r.cookies['cookies'] = cookies


# room id -> uid
def liver_uid(room_id):
    try:
        uid_get = requests.get(
            "https://api.live.bilibili.com/room/v1/Room/get_info?room_id=" +
            str(room_id)
        )
        uid = str(uid_get.json()['data']['uid'])
    except Exception as e:
        print('Get Room ID JSON Error:\n' + str(e))
        return
    return uid


# uid -> room id / user name
def user_info(uid):
    global lID
    try:
        info_get = requests.get(
            "https://api.bilibili.com/x/space/acc/info?mid=" +
            str(uid),
            headers=hd
        )
    except Exception as e:
        print('Get UID JSON Error:\n' + str(e))
        return
    info = info_get.json()
    try:
        lID = str(info['data']['name'])
    except Exception as e:
        print(str(e))
        print(str(info['message']))
    room_id = str(info['data']['live_room']['roomid'])
    return room_id, lID


# 获取直播间表情（包括UP主大表情）
def live_emoji(room_id):
    try:
        bq_get = r.get(
            "https://api.live.bilibili.com/xlive/web-ucenter/v2/emoticon/GetEmoticons?platform=pc&room_id="
            + str(room_id),
            headers=hd
        )
    except Exception as e:
        print('Get Room Emoji JSON Error:\n' + str(e))
        return
    return bq_get


# 获取充电表情（包括UP主大表情）
def charge_emoji(uid):
    try:
        bq_get = r.get(
            "https://api.bilibili.com/x/emote/creation/package/list?appkey=1d8b6e7d45233436&build=7080200&business"
            "=reply&mobi_app=android&up_mid="
            + str(uid),
            headers=hd
        )
    except Exception as e:
        print('Get Charge Emoji JSON Error:\n' + str(e))
        return
    return bq_get


def download_emoji(up_emoji_list, base_dir, emoji_type=''):
    for i, item in enumerate(up_emoji_list):
        img_name = item[0]
        try:
            # with open(base_dir + '/emoji/' + img_name + '.png', 'wb') as emoji_file:
            with open(base_dir + '/' + emoji_type + img_name + '.png', 'wb') as emoji_file:
                emoji_file.write(requests.get(item[1]).content)
        except OSError:
            # print('Name Error: Invalid Name')
            img_name = img_name.split('_')[0] + '_{}'.format(i)
            try:
                # with open(base_dir + '/emoji/' + img_name + '.png', 'wb') as emoji_file:
                with open(base_dir + '/' + emoji_type + img_name + '.png', 'wb') as emoji_file:
                    emoji_file.write(requests.get(item[1]).content)
            except:
                pass
        except Exception as e:
            print('Download Emoji Error:\n' + str(e))
            return
