from pydantic import BaseModel
from typing import Optional, List
from fastapi import Query


class User:
    def __init__(
        self,
        username: str = None,
        expansions: Optional[str] = None,
        user_fields : Optional[str] =  None,
        tweet_fields: Optional[List[str]] = Query(None)
    ):
        self.username = username
        self.expansions = expansions
        self.user_fields = user_fields
        self.tweet_fields = tweet_fields





