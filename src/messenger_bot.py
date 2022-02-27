from flask import Flask, request
import requests
from pymessenger import Bot

import tokens
from bot_functions import process_message

app = Flask(__name__)

# FB_API_URL = "https://graph.facebook.com/v2.6/me/messages"
PAGE_ACCESS_TOKEN = tokens.messenger_bot_page_access_token
VERIFY_TOKEN = tokens.user_verify_token

bot = Bot(PAGE_ACCESS_TOKEN)


@app.route("/", methods=["POST", "GET"])
def webhook():

    if request.method == "GET":
        """Veryfy user tokens equality"""
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        else:
            return "Not connected to fb"
            # is returned even being sucesfully conected

    elif request.method == "POST":
        """Respond to user input"""
        payload = request.json
        event = payload["entry"][0]["messaging"]

        for msg in event:
            text = msg["message"]["text"]
            sender_id = msg["sender"]["id"]
            response = process_message(text)
            bot.send_text_message(sender_id, response)

    else:
        print(request.data)
        return "200"


if __name__ == "__main__":
    app.run()
