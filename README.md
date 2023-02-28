# metrics 📈

[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg)](#contributors-)
[![Discord](https://img.shields.io/discord/669880381649977354?color=%237289da&label=Discord&logo=Discord)](https://discordapp.com/invite/MKXMSNC)
[![Subreddit subscribers](https://img.shields.io/reddit/subreddit-subscribers/developersIndia?style=social)](https://www.reddit.com/r/developersIndia/)

> Generate developersIndia Community Stats from Subreddit

Currently the stats are generated in following JSON format:

```json
{
    "totalMembers": 66600,
    "lastMonthUniquePageViews": 79519,
    "lastMonthTotalPageViews": 1286500,
    "yesterdayUniquePageViews": 18929,
    "yesterdayTotalPageViews": 71916,
    "discordTotalMembers": 7269,
    "discordTotalActiveMembers": 633
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
4. Export environment variables.
   * Reddit(Make sure you are have moderator privileges for the subreddit you want stats for).
      ```
      export REDDIT_CLIENT_ID=<YOU_REDDIT_APP_CLIENT_ID>
      export REDDIT_CLIENT_SECRET=<YOU_REDDIT_APP_CLIENT_SECRET>
      export REDDIT_PASSWORD=<REDDIT_PASSWORD>
      export REDDIT_USER=<REDDIT_USERNAME>
      ```
   * Discord(If possible set expiry to never)
      ```
      export DISCORD_INVITE_CODE=<YOUR_DISCORD_INVITE_CODE>
      ```
## Testing

Run the following command to run the test suite:
```bash
python -m unittest
```

## Resources & Learning Material 📚

- [PRAW Docs](https://praw.readthedocs.io/en/latest/code_overview/models/subreddit.html#praw.models.Subreddit.traffic)

# 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center"><a href="https://animesh-ghosh.github.io/"><img src="https://avatars.githubusercontent.com/u/34956994?v=4?s=100" width="100px;" alt=""/><br /><sub><b>MaDDogx</b></sub></a><br /><a href="https://github.com/developersIndia/metrics/commits?author=Animesh-Ghosh" title="Code">💻</a> <a href="https://github.com/developersIndia/metrics/commits?author=Animesh-Ghosh" title="Tests">⚠️</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
