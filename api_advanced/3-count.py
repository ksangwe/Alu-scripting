#!/usr/bin/python3
"""Recursively count keyword occurrences in hot post titles."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Print a sorted count of keywords found in hot post titles."""
    if counts is None:
        counts = {}
        for word in word_list:
            counts[word.lower()] = counts.get(word.lower(), 0)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api.advanced:v1.0.0 (by /u/ksangwe)"}
    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get("data")

    for post in data.get("children"):
        title = post.get("data").get("title").lower().split()
        for key in counts:
            counts[key] += title.count(key)

    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, counts)

    results = [(word, num) for word, num in counts.items() if num > 0]
    results = sorted(results, key=lambda x: (-x[1], x[0]))
    for word, num in results:
        print("{}: {}".format(word, num))
