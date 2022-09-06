# metrics

> Generate community stats from subreddit

## Scripts

### [main.py](https://github.com/developersIndia/metrics/blob/main/main.py)

Currently the stats are returned in following JSON format

```json
{
    "totalMembers": 66600,
    "lastMonthUniquePageViews": 79519,
    "lastMonthTotalPageViews": 1286500,
    "yesterdayUniquePageViews": 18929,
    "yesterdayTotalPageViews": 71916
}
```

## Setup

1. Clone the repo

   ```bash
   git clone https://github.com/developersIndia/metrics.git
   ```
2. Initialise a virtual environment.

   ```bash
   cd metrics
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

## Resources & Learning Material

- [PRAW Docs](https://praw.readthedocs.io/en/latest/code_overview/models/subreddit.html#praw.models.Subreddit.traffic)