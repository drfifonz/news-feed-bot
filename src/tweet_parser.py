import sys
from typing import List, Tuple, Union

from models.media import Media
from models.tweet import Tweet
from models.user import User

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

        self.data: list = response.get(DATA)

        includes: dict = response.get(INCLUDES)
        self.media: List[Media] = self._extract_media(includes)
        self.users: List[User] = self._extract_users(includes)
        self.tweets: List[Tweet] = self._extract_tweets()

    def _extract_media(self, includes: dict) -> List[Media]:
        media = includes.get(MEDIA)
        if media is None:
            return

        media_extracted = {}
        for media_item in media:
            media_key = media_item.get(MEDIA_KEY)
            media_extracted[media_key] = Media(
                media_key, media_item.get(TYPE), media_item.get(URL)
            )

        return media_extracted

    def _extract_tweets(self) -> list:
        tweets: List[Tweet] = []
        for tweet in self.data:
            tweet_id = tweet.get(ID)
            created_at = tweet.get(CREATED_AT)
            text = tweet.get(TEXT)
            author_id = tweet.get(AUTHOR_ID)

            attachments = tweet.get(ATTACHMENTS)
            if attachments is not None:
                media_keys = attachments.get(MEDIA_KEYS)
                if media_keys is not None:
                    medias: List[Media] = []
                    for key in media_keys:
                        medias.append(self.media[key])
            else:
                medias = None

            tweet = Tweet(tweet_id, created_at, text, author_id, medias)
            tweets.append(tweet)

            self.users[author_id].add_tweet(tweet)

        return tweets

    def _extract_users(self, includes: dict) -> List[User]:
        users = includes.get(USERS)
        if users is None:
            return

        users_extracted = {}
        for user in users:
            user_id = user.get(ID)
            users_extracted[user_id] = User(user_id, user.get(NAME))

        return users_extracted

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
