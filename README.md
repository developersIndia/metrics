# communityStats

> Generate community stats from subreddit


## Scripts

### [main.py](https://github.com/developersIndia/communityStats/blob/main/main.py)

Currently the stats are returned in following JSON format

```json
{
    "totalMembers": 65986,
    "traffic": [
        {
            "monthly": [
                {
                    "month": "Sep 2022",
                    "totalPageViews": 25708,
                    "uniquePageViews": 194731
                },
                {
                    "month": "Aug 2022",
                    "totalPageViews": 79519,
                    "uniquePageViews": 1286500
                },
                ...
            ]
        }
    ]
}
```

## Setup

1. Clone the repo

   ```bash
   git clone https://github.com/developersIndia/communityStats.git
   ```
2. Initialise a virtual environment.

   ```bash
   cd communityStats
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

## Resources & Learning Material

- [PRAW Docs](https://praw.readthedocs.io/en/stable/code_overview/other/idcard.html)