import os

import requests
from dotenv import load_dotenv
from flask import Flask, request
from pymessenger import Bot

from bot_functions import MessengerBot

load_dotenv()

# FB_API_URL = "https://graph.facebook.com/v2.6/me/messages"
PAGE_ACCESS_TOKEN = os.environ.get("messenger_bot_page_access_token")
VERIFY_TOKEN = os.environ.get("user_verify_token")

app = Flask(__name__)
bot = Bot(PAGE_ACCESS_TOKEN)


@app.route("/", methods=["POST", "GET"])
def webhook():
    if request.method == "GET":
        """Veryfy user tokens equality"""
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        else:
            return "incorrect token"  # Flask needs to get some response
    elif request.method == "POST":
        """Respond to user input"""
        payload = request.json
        event = payload["entry"][0]["messaging"]

        for msg in event:
            text = msg["message"]["text"]
            sender_id = msg["sender"]["id"]
            response = MessengerBot().process_message(text)
            bot.send_text_message(sender_id, response)
        return "200"
    else:
        print(request.data)
        return "200"


if __name__ == "__main__":
    # app.debug = True  # uncomment for debugging
    app.run()
