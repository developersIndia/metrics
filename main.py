'''
    This script is used for generating developersIndia subreddit traffic stats
'''
import praw
import os
import json
from datetime import datetime, timedelta
from discord import get_discord_stats
from utils import *

client_id = os.environ["REDDIT_CLIENT_ID"]
client_secret = os.environ["REDDIT_CLIENT_SECRET"]
reddit_pass = os.environ["REDDIT_PASSWORD"]
reddit_user = os.environ["REDDIT_USER"]

discord_invite_code = os.environ["DISCORD_INVITE_CODE"]

REPORT_PATH="data/index.json"

last_month = get_last_month()
last_day = get_last_day()

def generate_data(members, stats, discord_data):
    subreddit_stats = {}

    if members is not None:
        subreddit_stats["totalMembers"] = members

    for data in stats["month"]:
        datetime = get_readable_month(data[0])
        if datetime == last_month:
            subreddit_stats["lastMonthUniquePageViews"] = data[1]
            subreddit_stats["lastMonthTotalPageViews"] = data[2]

    for data in stats["day"]:
        datetime = get_readable_day(data[0])
        if datetime == last_day:
            subreddit_stats["yesterdayUniquePageViews"] = data[1]
            subreddit_stats["yesterdayTotalPageViews"] = data[2]

    # populate discord data to the stats.
    combined_stats = {**subreddit_stats, **discord_data}
    with open(REPORT_PATH, 'w') as report:
        json.dump(combined_stats, report, indent=4)

def find_traffic():
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        password=reddit_pass,
        user_agent="testscript",
        username=reddit_user,
    )
    stats = reddit.subreddit("developersIndia").traffic()
    members = reddit.subreddit("developersIndia").subscribers

    # Discord server data
    discord_stats = get_discord_stats(discord_invite_code)
    generate_data(members, stats, discord_stats)

if __name__ == '__main__':
    find_traffic()
