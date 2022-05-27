from aioflask import Flask, render_template, Response, request
import bot_function
import json
import asyncio

app = Flask(__name__)


async def write_json(data, filename='response.json'):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


@app.route("/")
async def index():
    return "Port:8443, Laogege is Coding"


@app.route('/webhook', methods=['POST', 'GET'])
async def webhook():
    if request.method == 'POST':
        webhook_message = json.loads(request.data)
        print(webhook_message)
        return webhook_message
    else:
        return "We don't support GET method"


@app.route("/bot", methods=['POST', 'GET'])
async def bot():
    if request.method == 'POST':
        webhook_message = request.get_json()
        await write_json(webhook_message, 'tg_request.json')
        print(webhook_message)
        chat_id = webhook_message['message']['chat']['id']
        message_id = webhook_message['message']['message_id']
        message_from_id = webhook_message['message']['from']['id']
        message_from_first_name = webhook_message['message']['from']['first_name']
        message_text = webhook_message['message']['text']
        text = str(message_text).upper()

        if message_from_id == chat_id:
            await bot_function.sendMessage(chat_id, message_text)
            return Response('ok', status=200)
        else:
            reply_message = f"{message_from_first_name} 你好呀，这条消息很奇怪，\nChat ID （{chat_id}）不等于 Message from ID（{message_from_id}），这个不应该啊。"
            await bot_function.sendMessage(chat_id, reply_message)
            return Response('ok', status=200)
    else:
        return f"Laogege's Coding Telegram Bot...\n'GET' method is not allowed."


if __name__ == '__main__':
    asyncio.run(app.run(host='0.0.0.0', port=8443, ssl_context=("fullchain.pem", "privkey.pem")))
