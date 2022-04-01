from typing import Optional, List
from fastapi import Query
import datetime



class UserTweet: 
    def __init__(
        self,
        username: str = None,
        end_time: Optional[datetime.datetime] = None,
        start_time: Optional[datetime.datetime] = None,
        exclude: Optional[List[str]] = Query(None),
        expansions: Optional[List[str]] = Query(None),
        media_fields: Optional[List[str]] = Query(None),
        poll_fields: Optional[List[str]] = Query(None),
        place_fields: Optional[List[str]] = Query(None),
        user_fields : Optional[List[str]] = Query(None),
        tweet_fields: Optional[List[str]] = Query(None),
        max_results: Optional[int] = None,
    ):
        self.username = username
        self.end_time = end_time
        self.start_time = start_time
        self.exclude = exclude
        self.expansions = expansions
        self.media_fields = media_fields
        self.poll_fields = poll_fields
        self.place_fields = place_fields
        self.user_fields = user_fields
        self.tweet_fields = tweet_fields
        self.max_results = max_results