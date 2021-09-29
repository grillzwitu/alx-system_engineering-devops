#!/usr/bin/python3
"""
The script queries the reddit api and returns
the number of subscribers for that subredit
"""

import requests
import sys


def number_of_subscribers(subreddit):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}
    info = requests.get(
        'http://www.reddit.com/r/{}/about.json'.format(subreddit),
        headers=headers).json()
    if info.get('kind') != 't5':
        return 0
    else:
        data = info.get('data')
        count = data.get('subscribers')
        return count
