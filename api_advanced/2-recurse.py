#!/usr/bin/python3
"""Recursively query the Reddit API for all hot post titles."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of all hot post titles for a subreddit, or None."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api.advanced:v1.0.0 (by /u/ksangwe)"}
    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data")
    for post in data.get("children"):
        hot_list.append(post.get("data").get("title"))

    after = data.get("after")
    if after is not None:
        return recurse(subreddit, hot_list, after)

    return hot_list
