"""
This script is used for generating developersIndia subreddit traffic stats
"""

import json
import os
from typing import Any, Dict, List

import praw

from discord import get_discord_stats
from utils import get_last_day, get_last_month, get_readable_day, get_readable_month


# Get credentials from env
client_id = os.getenv("REDDIT_CLIENT_ID")
client_secret = os.getenv("REDDIT_CLIENT_SECRET")
reddit_pass = os.getenv("REDDIT_PASSWORD")
reddit_user = os.getenv("REDDIT_USER")
discord_invite_code = os.getenv("DISCORD_INVITE_CODE")

# validate that all credentials are present
if not client_id or not client_secret or not reddit_pass or not reddit_user:
    raise RuntimeError("Missing reddit credentials")

if not discord_invite_code:
    raise RuntimeError("Missing DISCORD_INVITE_CODE")


REPORT_PATH = "data/index.json"

last_month = get_last_month()
last_day = get_last_day()


def generate_data(
    members: int | None,
    stats: Dict[str, List[List[int]]],
    discord_stats: Dict[str, Any],
):
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
    combined_stats = {**subreddit_stats, **discord_stats}
    with open(REPORT_PATH, "w", encoding="utf-8") as report:
        json.dump(combined_stats, report, indent=4)


def find_traffic():
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        password=reddit_pass,
        user_agent="testscript",
        username=reddit_user,
    )
    stats: Dict[str, List[List[int]]] = reddit.subreddit("developersIndia").traffic()
    members: int = reddit.subreddit("developersIndia").subscribers

    # Discord server data
    discord_stats: Dict[str, Any] = get_discord_stats(discord_invite_code)
    generate_data(members, stats, discord_stats)


if __name__ == "__main__":
    find_traffic()
