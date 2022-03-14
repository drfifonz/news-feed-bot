import sys
from typing import Tuple, Union


DATA = "data"
ERRORS = "errors"
INCLUDES = "includes"
MESSAGE = "message"
MEDIA = "media"
USERS = "users"

ATTACHMENTS = "attachments"
AUTHOR_ID = "author_id"
CREATED_AT = "created_at"
ID = "id"
MEDIA_KEY = "media_key"
MEDIA_KEYS = "media_keys"
NAME = "name"
TEXT = "text"
TYPE = "type"
URL = "url"

class TweetParser:
    def __init__(self, response: dict) -> None:
        self._handle_errors(response)

        self.data: Union[dict, list] = response.get(DATA)

        includes: dict = response.get(INCLUDES)
        self.media: Union[dict, list] = includes.get(MEDIA, [])
        self.users: Union[dict, list] = includes.get(USERS, [])

        self.tweets = self._extract_tweets(response)

    def _extract_tweets(self, tweet_json: dict) -> list:
        attachments = tweet_json.get(ATTACHMENTS)
        self.media_keys = attachments.get(MEDIA_KEYS) if attachments else None

    def _get_author_name(self, author_id) -> str:
        if type(self.users) == dict:
            return self.users[NAME]

        elif type(self.users) == list:
            for user in self.users:
                if user.get(ID, -1) == author_id:
                    return user.get(NAME)

        else:
            raise TypeError(
                f"Expected type of 'users' is dict or list but is {type(self.users)}"
            )

    def _get_media(self, media_key) -> Tuple[str, str]:
        if type(self.media) == dict:
            return self.media.get(TYPE), self.media.get(URL) 

        elif type(self.media) == list:
            for media_item in self.media:
                if media_item.get(MEDIA_KEY) == media_key:
                    return media_item.get(TYPE), media_item.get(URL)

        else:
            raise TypeError(
                f"Expected type of 'media' is dict or list but is {type(self.media)}"
            )

    def _handle_errors(self, response):
        errors = response.get(ERRORS)
        if errors is None:
            return

        print(errors.get(MESSAGE))
        sys.exit(-1)
