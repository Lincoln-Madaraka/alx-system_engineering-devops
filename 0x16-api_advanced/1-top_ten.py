#!/usr/bin/python3
'''Module for task 1'''
import requests


def top_ten(subreddit):
    '''Return the top 10 hot post for a given subreddit'''
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Myscript/2.0 (by /u/kirlos)'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data').get('children')
        for i in range(10):
            print(data[i].get('data').get('title'))
    else:
        print(None)
