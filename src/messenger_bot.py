import os
import sys
import time
from unittest import skip

import requests
from dotenv import load_dotenv
from flask import Flask, request

# from pymessenger import Bot

from bot_functions import MessengerBot

load_dotenv()

# FB_API_URL = "https://graph.facebook.com/v13.0/me/messages"
PAGE_ACCESS_TOKEN = os.environ.get("MESSENGER_BOT_PAGE_ACCESS_TOKEN")
VERIFY_TOKEN = os.environ.get("USER_VERIFY_TOKEN")

app = Flask(__name__)
bot = MessengerBot(PAGE_ACCESS_TOKEN)


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
        # print(payload, file=sys.stderr)
        bot.process_message(payload)
        return "200"

    else:
        print(request.data)
        return "200"


if __name__ == "__main__":

    # app.debug = True  # uncomment for debugging
    app.run(
        host="0.0.0.0", port=os.environ.get("PORT", 5000)
    )  # importent to predefine host & port for working on heroku
