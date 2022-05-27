# flask_webhook_telegram_bot

Using flask webhook function to work with telegram bot api.

目标：
- 首先是通过自己搭建Webhook服务器的形式实现Telegram Bot API的通信
- 第二是直接通过URL与Telegram API交流，不使用第三方的库。

注意事项：
- Telegram Bot API只能注册到HTTPS服务器，所以必须完成SSL认证
- 如果Webhook服务器的443端口要跑Web服务，就只能开8443端口，TG也是支持的
- 如果需要设置Async功能，则需要 pip install aioflask 替代 flask
- 总体感觉上线后消息速度比Telegram自己的服务器慢（Polling的效果）

Telegram Bot API注册自己的Webhook服务器，直接在浏览器输入以下地址，回车即可得到反馈：

https://api.telegram.org/bot<Your Bot API, 括号需要去掉>/setWebhook?url=https://<Your Webhook Server URL,可以带端口号，域名需要完成SSL签名，括号需要去掉>

今天忙了一天，解决了各种小问题，终于成功了，分享给大家。

我主要也是参考了一个老外的Youtube视频，这里顺便分享给大家。

https://www.youtube.com/watch?v=XiBA5LRQFLM
