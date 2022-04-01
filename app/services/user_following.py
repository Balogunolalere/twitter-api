from config import client
from typing import Optional, List






def get_user_following(
    
        username: str = None,
        expansions: Optional[List[str]] = None,
        user_fields : Optional[List[str]] = None,
        tweet_fields: Optional[List[str]] = None,
        max_results: Optional[int] = None,
):
    
    follower = client.get_users_following(
        id=client.get_user(username=username).json()['data']['id'],
        expansions=expansions,
        user_fields=user_fields,
        tweet_fields=tweet_fields,
        max_results=max_results,
    )
    return follower
                