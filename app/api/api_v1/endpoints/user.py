from fastapi import APIRouter, Depends, Query
from app.models.user_model import User
from app.models.user_follow_model import Followers, Following
from app.models.user_tweets_model import UserTweet
from app.services.user_tweet import get_user_tweets
from app.services.user_following import get_user_following
from app.services.search_user import search_user
from app.services.user_follower import get_user_followers
from typing import Optional


router = APIRouter()


@router.get('/', tags=['User'])
def get_user(user: User = Depends(User)):
    resp = search_user(user.username, user.expansions, user.user_fields, user.tweet_fields)
    if resp is not None:
        return resp.json()
    
    else:
        resp
    
@router.get('/followers', tags=['User'])
def get_users_followers(follow: Followers = Depends(Followers)):
    resp = get_user_followers(follow.username, follow.expansions, follow.user_fields, follow.tweet_fields, follow.max_results)
    if resp is not None:
        return resp.json()
    
    else:
        resp
        
@router.get('/following', tags=['User'])
def get_users_following(following: Following = Depends(Following)):
    resp = get_user_following(following.username, following.expansions, following.user_fields, following.tweet_fields, following.max_results)
    if resp is not None:
        return resp.json()
    
    else:
        resp


@router.get('/tweets', tags=['User'])
def get_user_all_tweets(tweet: UserTweet = Depends(UserTweet)):
    resp = get_user_tweets(tweet.username, tweet.end_time, tweet.start_time, tweet.exclude, tweet.expansions, tweet.media_fields, tweet.poll_fields, tweet.place_fields, tweet.user_fields, tweet.tweet_fields, tweet.max_results)
    if resp is not None:
        return resp.json()
    
    else:
        resp