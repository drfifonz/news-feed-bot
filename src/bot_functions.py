from pymessenger import Bot

import json

DEFINED_COMMANDS_PATH = "data/commands.json"

BOT_COMMANDS = "commands"
USER_TO_BOT_INPUT = "input"
BOT_TO_USER_OUTPUT = "output"


class MessengerBot:
    def __init__(self, page_access_token) -> None:
        self.bot = Bot(page_access_token)

    def load_json_file(self, path: str) -> dict:
        """Returns dictionary from .json file"""
        with open(path) as file:
            data = json.load(file)

        return data

    def answear_text_message(self, text: str) -> str:
        """:>"""

        formatted_message = text.lower().strip()

        data = self.load_json_file(DEFINED_COMMANDS_PATH)

        for sentence in data[BOT_COMMANDS]:
            if formatted_message == sentence[USER_TO_BOT_INPUT]:
                return sentence[BOT_TO_USER_OUTPUT]

    def process_message(self, payload: dict) -> None:
        """:>"""
        event = payload["entry"][0]["messaging"]
        sender_id = self.get_sender_id(event)
        for msg in event:
            text = msg["message"].get("text")
            if text is None:
                continue
            response = self.answear_text_message(text)
            self.bot.send_text_message(sender_id, response)

    def get_sender_id(self, event: dict) -> int:
        return event[0]["sender"]["id"]

    def cyclic_messaging(self, time_type, trigger: bool = 0, interval: int = 1) -> None:
        pass
