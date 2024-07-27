import tweepy
import os
from dotenv import load_dotenv
import requests

load_dotenv()

consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")


# Authenticate with the v2.0 API
def two_auth(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
):
    """Returns the tweepy v2.0 Client class object for creating tweets."""
    client = tweepy.Client(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )
    print("X API v2.0 authentication successful.")
    return client


# Post the content to X
def create_tweet(auth_client, content):
    try:
        response = auth_client.create_tweet(text=content)
        print("Tweet posted successfully.")
        return response
    except Exception as e:
        print(f"Error posting tweet: {e}")
        return None


#  Pipeline function to post tweets to X
def post_tweet(tweet_body):
    # Get API v2.0 authentication to create tweets
    client_auth = two_auth()

    # Create the tweet
    try:
        response = create_tweet(client_auth, tweet_body)
        if response:
            return True
    except Exception as e:
        print(f"Failed to post tweet: {e}")
    return False
