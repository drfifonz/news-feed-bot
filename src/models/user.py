from typing import List

from models.tweet import Tweet


class User:
    def __init__(self, user_id, user_name) -> None:
        self._user_id: int = user_id
        self._user_name: str = user_name
        self._tweets: list[Tweet] = []

    def add_tweet(self, tweet: Tweet) -> None:
        self._tweets.append(tweet)

    def get_id(self) -> int:
        return self._user_id

    def get_name(self) -> str:
        return self._user_name

    def get_tweets(self) -> List[Tweet]:
        return self._tweets

