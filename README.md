# metrics 📈

> Generate devsIndia Community Stats from Subreddit

Currently the stats are generated in following JSON format:

```json
{
    "totalMembers": 66600,
    "lastMonthUniquePageViews": 79519,
    "lastMonthTotalPageViews": 1286500,
    "yesterdayUniquePageViews": 18929,
    "yesterdayTotalPageViews": 71916
}
```

## Setup 👷

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
4. Export environment variables. (Make sure you are have moderator privileges for the subreddit you want stats for).
   ```
   export REDDIT_CLIENT_ID=<YOU_REDDIT_APP_CLIENT_ID>
   export REDDIT_CLIENT_SECRET=<YOU_REDDIT_APP_CLIENT_SECRET>
   export REDDIT_PASSWORD=<REDDIT_PASSWORD>
   export REDDIT_USER=<REDDIT_USERNAME>
   ```

## Resources & Learning Material 📚

- [PRAW Docs](https://praw.readthedocs.io/en/latest/code_overview/models/subreddit.html#praw.models.Subreddit.traffic)

# 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
