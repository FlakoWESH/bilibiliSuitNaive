# Live_emoji分支（未实现，开发中）

获取UP主大表情和房间专属表情，通过直播间号识别

## 实现方式

根据网页响应JSON保存相应媒体资源。

使用API：

> https://api.live.bilibili.com/xlive/web-ucenter/v2/emoticon

请求方式：GET

请求头：

- "room_id"

返回格式：JSON

---

## 运行方式

1. 使用Python脚本运行：请确保 Python 环境已安装`requests`，确保安装之后运行`main.py`即可
2. 使用二进制文件直接运行：双击`BiliSuitGet.exe`运行即可。由于缺少编译环境故只编译了Windows版本，其他版本建议使用Python源文件直接运行

## 使用说明

程序支持简单的表情获取，输入主播房间号即可

## 已知问题

1. 使用代理进行访问时可能会出现无响应的情况

2. 部分素材由于包含非法字符无法以原名称保存

---

## 注意事项

1. 程序仅供学习参考，请在下载后 24 小时内删除
2. 请不要短时间内进行大量操作，否则可能有 IP 封禁等风险
3. 请不要将脚本及脚本产生内容用作商业用途
4. 程序未经标准测试，可能在运行中产生 bug，请不要使用奇怪的姿势试探 bug

## 致谢

程序编写时参考的项目列表

- [SocialSisterYi/bilibili-API-collect](https://github.com/SocialSisterYi/bilibili-API-collect)

虽然该 API 集合中未找到程序所依赖的 API，但这一项目提供了本程序的最初构想。本程序所依赖的 API 通过 js 分析法得到。
