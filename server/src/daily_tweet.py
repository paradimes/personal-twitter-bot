import requests
from post_tweet import post_tweet


def get_quote():
    response = requests.get("https://zenquotes.io/api/today")
    json_data = response.json()
    if json_data and len(json_data) > 0:
        quote = json_data[0]["q"]
        author = json_data[0]["a"]
        tweet_quote = f'"{quote}" - {author}'
        return tweet_quote
    else:
        print("Failed to fetch quote from API")
        return None


# Daily tweet with quote
def daily_tweet():
    tweet_quote = get_quote()
    tweet_body = f"@projectanas Lock in.\n\n{tweet_quote}"
    post_tweet(tweet_body=tweet_body)


if __name__ == "__main__":
    daily_tweet()
