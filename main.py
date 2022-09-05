'''
    This script is used for generating developersIndia subreddit traffic stats
'''
import praw
import os
import pprint
import time
import json

client_id = os.environ["REDDIT_CLIENT_ID"]
client_secret = os.environ["REDDIT_CLIENT_SECRET"]
reddit_pass = os.environ["REDDIT_PASSWORD"]

REPORT_PATH="data/index.json"

def get_readable_date(unix_t):
    t = time.localtime(unix_t)
    # Format: 'Apr, 2021'
    return time.strftime("%b %Y", t)

def generate_data(members, stats):
    subreddit_stats = {}
    # pprint.pprint(stats)
    if members is not None:
        subreddit_stats["totalMembers"] = members

    if stats is not None:
        subreddit_stats["traffic"] = []

    monthly_list = []
    for data in stats["month"]:
        monthly_stats = {}
        if data is not None:
            datetime = get_readable_date(data[0])
            monthly_stats["month"] = datetime
            monthly_stats["totalPageViews"] = data[1]
            monthly_stats["uniquePageViews"] = data[2]
            monthly_list.append(monthly_stats)
    
    subreddit_stats["traffic"].append({"monthly": monthly_list})

    with open (REPORT_PATH, 'w') as report:
        json.dump(subreddit_stats, report, indent=4)

    # print(f"Date: {datetime}, Total PageViews: {data[1]}, Unique PageViews: {data[2]}")

def find_traffic():
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        password=reddit_pass,
        user_agent="testscript by u/BhupeshV",
        username="BhupeshV",
    )
    stats = reddit.subreddit("developersIndia").traffic()
    members = reddit.subreddit("developersIndia").subscribers
    generate_data(members, stats)

if __name__ == '__main__':
    find_traffic()
