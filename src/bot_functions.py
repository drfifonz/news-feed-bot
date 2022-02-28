import json

DEFINED_COMMANDS_PATH = "pl-PL.json"

BOT_COMMANDS = "commands"
USER_TO_BOT_INPUT = "input"
BOT_TO_USER_OUTPUT = "output"


class MessengerBot:
    def load_json_file(self, path: str) -> dict:
        """Returns dictionary from .json file"""
        with open(path) as file:
            data = json.load(file)

        return data

    def process_message(self, text: str) -> str:
        """Processing user input, returning proper response"""

        formatted_message = text.lower().strip()

        data = self.load_json_file(DEFINED_COMMANDS_PATH)

        for sentence in data[BOT_COMMANDS]:
            if formatted_message == sentence[USER_TO_BOT_INPUT]:
                return sentence[BOT_TO_USER_OUTPUT]
