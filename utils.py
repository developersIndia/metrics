import time
from datetime import datetime, timedelta

def get_last_month():
    now = datetime.now()
    last_month = now - timedelta(weeks=4)
    return last_month.strftime("%-m %Y")

def get_last_day():
    now = datetime.now()
    last_day = now - timedelta(days=1)
    return last_day.strftime("%d/%-m/%Y")

def get_readable_month(unix_t):
    t = time.localtime(unix_t)
    # Format: '9, 2021'
    return time.strftime("%-m %Y", t)

def get_readable_day(unix_t):
    t = time.localtime(unix_t)
    # Format: '03/12/2021'
    return time.strftime("%d/%-m/%Y", t)