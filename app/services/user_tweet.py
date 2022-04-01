import datetime

from typing import Optional, List
from config import client

   

def get_user_tweets(
    username: str = None,
    end_time: Optional[datetime.datetime] = None,
    start_time: Optional[datetime.datetime] = None,
    exclude: Optional[List[str]] = None,
    expansions: Optional[List[str]] = None,
    media_fields: Optional[List[str]] = None,
    poll_fields: Optional[List[str]] = None,
    place_fields: Optional[List[str]] = None,
    user_fields : Optional[List[str]] = None,
    tweet_fields: Optional[List[str]] = None,
        max_results: Optional[int] = None,
):
    
    tweet = client.get_users_tweets(
        id=client.get_user(username=username).json()['data']['id'],
        max_results=max_results,
        tweet_fields=tweet_fields,
        user_fields=user_fields,
        place_fields=place_fields,
        poll_fields=poll_fields,
        media_fields=media_fields,
        expansions=expansions,
        exclude=exclude,
        start_time=start_time,
        end_time=end_time,
    )
    return tweet
                                        