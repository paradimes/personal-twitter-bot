# Personal Twitter Bot

This project is a Python-based Twitter bot that automatically posts daily inspirational quotes and weekly prompts.

## Features

- Daily tweet: Posts an inspirational quote from the Zen Quotes API
- Weekly tweet: Posts a productivity prompt every Sunday

## Technical Details

- Built with Python 3
- Uses Tweepy for Twitter API interaction
- Fetches quotes from Zen Quotes API
- Configured for deployment on a VPS with cron jobs

## Setup

1. Clone the repository
2. Create a virtual environment and activate it: `python3 -m venv venv` and `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Set up a Twitter Developer account and create an app. Ensure you've configured Read/Write permissions as it's Read only by default.
5. Create a `.env` file with your Twitter API credentials
6. Create a shell script `run_twitter_bot.sh` with your project path and relevant commands. Make the script executable: `chmod +x /path/to/your/twitter_bot_project/run_twitter_bot.sh`
7. Set up cron jobs to run the script at desired intervals: `crontab -e`

`run_twitter_bot.sh`

```sh
#!/bin/bash

# Set the path to your project directory
PROJECT_DIR="/path/to/your/twitter_bot_project"

# Activate virtual environment
source "$PROJECT_DIR/venv/bin/activate"

# Function to run a script
run_script() {
    python "$PROJECT_DIR/src/$1"
}

# Check which script to run based on the argument
if [ "$1" == "daily" ]; then
    run_script "daily_tweet.py"
elif [ "$1" == "weekly" ]; then
    run_script "weekly_tweet.py"
else
    echo "Invalid argument. Use 'daily' or 'weekly'."
    exit 1
fi

# Deactivate virtual environment
deactivate
```

`crontab`

```sh
# Twitter Bot: Daily tweet at 9AM EST (14:00 UTC)
0 14 * * * /path/to/your/twitter_bot_project/run_twitter_bot.sh daily

# Twitter Bot: Weekly tweet at 9PM EST on Sundays (02:00 UTC Monday)
0 2 * * 1 /path/to/your/twitter_bot_project/run_twitter_bot.sh weekly
```

## Usage

The bot can be run manually with:

```bash
./run_twitter_bot.sh daily
./run_twitter_bot.sh weekly
```

For automatic posting, configure cron jobs on your server.
Note
Remember to keep your .env file secret and never commit it to version control.
