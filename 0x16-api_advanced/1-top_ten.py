#!/usr/bin/python3
"""
The script queries the reddit api and prints
the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}
    params = {"limit": 10}
    info = requests.get(
        "http://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers=headers, params=params)
    if info.status_code == 404:
        print('None')
        return
    r = info.json().get("data")
    [print(i.get("data").get("title")) for i in r.get("children")]
