from requests import get
from os.path import exists
from os import makedirs


def get_suit(suit_id, base_dir='./'):
    """
    获取单个装扮素材

    输入:
        - suit_id: 装扮ID
        - base_dir: 保存路径

    输出: 素材文件夹
    """
    final_status = 100
    try:
        rq_get = get(
            "https://api.bilibili.com/x/garb/v2/mall/suit/detail?item_id="
            + str(suit_id)
        )
    except Exception as e:
        print('Get JSON Error:\n' + str(e) + '\n')
        return

    res = rq_get.json()

    if res['data']['item_id'] == 0:
        print('Cannot find certain suit.')
        return

    # ./装扮名作为路径
    base_dir += res['data']['name']

    # Save suit json
    if not exists(base_dir):
        makedirs(base_dir)
    with open(base_dir + '/suit_info.json', 'w', encoding='utf-8') as suit_json_file:
        suit_json_file.write(rq_get.text)

    # Part 1. Emoji
    emoji_list = [
        (item['name'][1:-1], item['properties']['image'])
        for item in res['data']['suit_items']['emoji_package'][0]['items']
    ]
    # """
    for i, item in enumerate(emoji_list):
        img_name = item[0]
        try:
            # with open(base_dir + '/emoji/' + img_name + '.png', 'wb') as emoji_file:
            with open(base_dir + '/' + img_name + '.png', 'wb') as emoji_file:
                emoji_file.write(get(item[1]).content)
        except OSError:
            print('Name Error: Invalid Name')
            img_name = img_name.split('_')[0] + '_{}'.format(i)
            try:
                # with open(base_dir + '/emoji/' + img_name + '.png', 'wb') as emoji_file:
                with open(base_dir + '/' + img_name + '.png', 'wb') as emoji_file:
                    emoji_file.write(get(item[1]).content)
            except:
                pass
            final_status = 101
        except Exception as e:
            print(str(e))
            return
    # """

    # Part 2. Background
    bg_dict = res['data']['suit_items']['space_bg'][0]['properties']
    bg_list = list()
    for key, value in bg_dict.items():
        if key != 'fan_no_color':
            # if key[0] == 'i':
            bg_list.append((key, value))
    # """
    if not exists(base_dir + '/background/'):
        makedirs(base_dir + '/background/')
    for item in bg_list:
        try:
            with open(base_dir + '/background/' + item[0] + '.jpg',
                      'wb') as bg_file:
                bg_file.write(get(item[1]).content)
        except Exception as e:
            print('Background Error:\n' + str(e))
            return
            # """

    # Part 3. Others
    pro_list = [
        ('properties.zip', res['data']['suit_items']['skin'][0]['properties']['package_url']),
        ('fan_share_image.jpg', res['data']['properties']['fan_share_image']),
        ('image_cover.jpg', res['data']['properties']['image_cover']),
        ('avatar.jpg', res['data']['fan_user']['avatar']),
        ('emoji.png', res['data']['suit_items']['emoji_package'][0]['properties']['image'])
    ]
    # """
    try:
        pro_list.append(('image_cover_long.png', res['data']['properties']['image_cover_long']))
    except:
        pass
    if not exists(base_dir + '/properties/'):
        makedirs(base_dir + '/properties/')
    for item in pro_list:
        try:
            with open(base_dir + '/properties/' + item[0], 'wb') as pro_file:
                pro_file.write(get(item[1]).content)
        except Exception as e:
            print('Properties Error:\n' + str(e))
            return
    # """

    # Part 4. Card
    card_list = [
        # ('fans_image', res['data']['suit_items']['card'][0]['properties']['fans_image']),
        # ('bg_image', res['data']['suit_items']['card_bg'][0]['properties']['image']),
        ('card_bg_preview', res['data']['suit_items']['card_bg'][0]['properties']['image_preview_small'])
    ]
    try:
        card_list.append(
            ('card_fans', res['data']['suit_items']['card'][0]['properties']['fans_image'])
        )
    except:
        pass
    try:
        card_list.append(
            ('card_preview', res['data']['suit_items']['card'][0]['properties']['image_preview_small'])
        )
        card_list.append(
            ('card', res['data']['suit_items']['card'][1]['properties']['image'])
        )
    except:
        pass
    try:
        card_list.append(
            ('card_preview', res['data']['suit_items']['card'][1]['properties']['image_preview_small'])
        )
        card_list.append(
            ('card', res['data']['suit_items']['card'][0]['properties']['image'])
        )
    except:
        pass

    # """
    if not exists(base_dir + '/properties/'):
        makedirs(base_dir + '/properties/')
    for item in card_list:
        try:
            with open(base_dir + '/properties/' + item[0] + '.png',
                      'wb') as card_file:
                card_file.write(get(item[1]).content)
        except Exception as e:
            print('Card Error:\n' + str(e))
            return
    # """

    # Part 5. Loading
    if 'loading' in res['data']['suit_items']:
        ld_list = [
            ('loading_preview.png', res['data']['suit_items']['loading'][0]['properties']['image_preview_small']),
            ('loading_frame_url.png', res['data']['suit_items']['loading'][0]['properties']['loading_frame_url']),
            ('loading_url.webp', res['data']['suit_items']['loading'][0]['properties']['loading_url'])
        ]
        # """""""""
        for item in ld_list:
            try:
                with open(base_dir + '/properties/' + item[0], 'wb') as ld_file:
                    ld_file.write(get(item[1]).content)
            except Exception as e:
                print('Loading Error\n' + str(e))
                return
        # """

    # Part 6. Play icon
    if 'play_icon' in res['data']['suit_items']:
        pl_dict = res['data']['suit_items']['play_icon'][0]['properties']
        pl_list = list()
        for key, value in pl_dict.items():
            if key != 'ver':
                # if key[0] == 'i':
                pl_list.append((key, value))
        # """""""""
        if not exists(base_dir + '/Play_icon/'):
            makedirs(base_dir + '/Play_icon/')
        for item in pl_list:
            try:
                with open(base_dir + '/Play_icon/' + item[0] + '.png',
                          'wb') as pl_file:
                    pl_file.write(get(item[1]).content)
            except Exception as e:
                print('Play Icon Error:\n' + str(e))
                return

        # """

    # Part 7. Thumb up
    if 'thumbup' in res['data']['suit_items']:
        thumb_list = [
            ('image_ani.bin', res['data']['suit_items']['thumbup'][0]['properties']['image_ani']),
            ('image_ani_cut.bin', res['data']['suit_items']['thumbup'][0]['properties']['image_ani_cut']),
            ('image_preview.png', res['data']['suit_items']['thumbup'][0]['properties']['image_preview'])
        ]
        # """""""""
        if not exists(base_dir + '/Thumb_up/'):
            makedirs(base_dir + '/Thumb_up/')
        for item in thumb_list:
            try:
                with open(base_dir + '/Thumb_up/' + item[0], 'wb') as thumb_file:
                    thumb_file.write(get(item[1]).content)
            except Exception as e:
                print('Thumb up Error: \n' + str(e))
                return
        # """

    return res, final_status


while True:
    mid = eval(input("input suit id: ").strip())
    get_suit(mid)
