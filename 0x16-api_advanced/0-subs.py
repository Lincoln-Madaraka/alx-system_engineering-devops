#!/usr/bin/python3
'''Module for task 0'''
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit."""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'User-Agent': 'Myscript/1.0 (by /u/kirlos)'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    return 0

