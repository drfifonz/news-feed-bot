from __future__ import annotations

from datetime import datetime
from typing import List

from models.media import Media

TWEET_URL = "https://twitter.com/Ukraine/status/{}"


class Tweet:
    def __init__(
        self,
        tweet_id: int,
        created_at: str,
        text: str,
        author_id: int,
        medias: List[Media],
    ) -> None:
        self.tweet_id: int = tweet_id
        self.created_at: str = created_at
        self.text: str = text
        self.author_id: int = author_id
        self.medias: List[Media] = medias

    def get_datetime_created(self) -> str:
        """
        Formats created_at (that should be in a date format provided by Twitter, eg. 2022-03-14T19:12:18.000Z) to datetime object.
        """
        return datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%S.%fZ")

    def __str__(self) -> str:
        return f"{self.tweet_id} - {self.get_datetime_created()} - {self.author_id} - {self.medias[0]}:\n{self.text}"


if __name__ == "__main__":
    tweet = Tweet(
        tweet_id=1,
        created_at="2020-03-14T19:12:18.000Z",
        text="Test tweet",
        author_id=1,
        medias=[],
    )
    print(tweet.get_datetime_created())
