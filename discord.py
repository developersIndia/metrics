import httpx
from typing import Dict, Any

DISCORD_INVITE_HACK_URL = 'https://discord.com/api/v9/invites/{invite_code}?with_counts=true&with_expiration=true'

def get_discord_stats(invite_code: str) -> Dict[str, Any]:
    discord_stats = {}
    res = httpx.get(DISCORD_INVITE_HACK_URL.format(invite_code=invite_code))
    if res.status_code == 200:
        res_json = res.json()
        discord_stats['discordTotalMembers'] = res_json.get('approximate_member_count')
        discord_stats['discordTotalActiveMembers'] = res_json.get(
            'approximate_presence_count'
        )

    return discord_stats
