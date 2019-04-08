from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('rKIlriekjYPT47zqWz92H6OFqexstOdA4BHGrhc6LlPT+z6hLQHAi5e67UQylh+3JkxPfKAEpd5I6yWD+O5Iruqgq7ZYKkoqDjIhH9f2/Emzx/TmKFdRPrx8Lzf+ufQD3w3cXDShu1gWdNA1766VeAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0c424f7e7ee4b4774cde3409e2bb3a22')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='OK'))


if __name__ == "__main__":
    app.run()