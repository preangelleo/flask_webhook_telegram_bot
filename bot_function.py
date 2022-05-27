from urllib.parse import urlencode
import time
import requests
import telegram_bots_api


base_url = "https://api.telegram.org/bot"+telegram_bots_api.MyFirstNodejsTgBot+"/"


async def sendMessage(chat_id, message):
    method = "sendMessage?"
    _params = {
        "parse_mode": "Markdown",
        "disable_web_page_preview": True,
        "disable_notification": True
    }
    params = urlencode(_params)
    URL = base_url + method + "chat_id=" + str(chat_id) + "&" + params + "&text=" + message
    print(URL)
    r = requests.post(URL)
    print(r)
    return "successfully sent"


async def deleteMessage(chat_id, message_id):
    method = "deleteMessage?"
    URL = base_url + method + "chat_id=" + str(chat_id) + "&message_id=" + str(message_id)
    print(URL)
    result = requests.post(URL)
    print(result)
    return result.ok


async def deleteLater(seconds, chat_id, message_id):
    time.sleep(seconds)
    await deleteMessage(chat_id, message_id + 1)
    await deleteMessage(chat_id, message_id)

