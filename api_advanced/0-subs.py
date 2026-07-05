#!/usr/bin/python3
"""Query the Reddit API for a subreddit's total subscriber count."""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit, or 0."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting:0-subs:v1.0 (by /u/ksangwe)"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json().get("data")
    if data is None:
        return 0

    return data.get("subscribers", 0)
