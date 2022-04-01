from config import client
from typing import Optional, List





def search_user(
    username: str = None,
    expansions: Optional[str] = None,
    user_fields: Optional[str] = None,
    tweet_fields: Optional[List[str]] = None
):
    if expansions is not None:
        if user_fields is not None:
            if tweet_fields is not None:
                user = client.get_user(username=username,
                                       expansions=expansions,
                                       user_fields=user_fields,
                                       tweet_fields=tweet_fields)
                return user
            else:
                user = client.get_user(username=username,
                                       expansions=expansions,
                                       user_fields=user_fields,
                                       )
                return user
        elif tweet_fields is not None:
            user = client.get_user(username=username,
                                   expansions=expansions,
                                   tweet_fields=tweet_fields)
            return user
        else:
            user = client.get_user(username=username,
                                   expansions=expansions)
            return user
    elif user_fields is not None:
        if tweet_fields is not None:
            user = client.get_user(username=username,
                                   user_fields=user_fields,
                                   tweet_fields=tweet_fields)
            return user
        else:
            user = client.get_user(username=username,
                                   user_fields=user_fields,
                                  )
            return user
    elif tweet_fields is not None:
        user = client.get_user(username=username,
                                   tweet_fields=tweet_fields)
        return user
    else:
        user = client.get_user(username=username,
                                   )
        return user
        