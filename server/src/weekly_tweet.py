from post_tweet import post_tweet


def weekly_tweet():
    tweet_body = "@projectanas What did you get done this week?"
    post_tweet(tweet_body=tweet_body)


if __name__ == "__main__":
    weekly_tweet()
