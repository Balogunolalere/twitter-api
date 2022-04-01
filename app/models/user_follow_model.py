from typing import Optional, List
from fastapi import Query


class Followers:
    def __init__(
        self,
        username: str = None,
        expansions: Optional[List[str]] = Query(None),
        user_fields : Optional[List[str]] = Query(None),
        tweet_fields: Optional[List[str]] = Query(None),
        max_results: Optional[int] = None,
    ):
        self.username = username
        self.expansions = expansions
        self.user_fields = user_fields
        self.tweet_fields = tweet_fields
        self.max_results = max_results


class Following:
    def __init__(
        self,
        username: str = None,
        expansions: Optional[List[str]] = Query(None),
        user_fields : Optional[List[str]] = Query(None),
        tweet_fields: Optional[List[str]] = Query(None),
        max_results: Optional[int] = None,
    ):
        self.username = username
        self.expansions = expansions
        self.user_fields = user_fields
        self.tweet_fields = tweet_fields
        self.max_results = max_results




