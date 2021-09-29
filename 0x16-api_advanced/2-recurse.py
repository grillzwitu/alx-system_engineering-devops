#!/usr/bin/python3
"""
The script returns a list containing the
titles of all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}
    params = {"after": after, "count": count, "limit": 100}
    info = requests.get(
        "http://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers=headers, params=params)
    if info.status_code == 404:
        return None
    r = info.json().get("data")
    after = r.get("after")
    count += r.get("dist")
    children = r.get("children")
    [hot_list.append(i.get("data").get("title")) for i in children]
    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
