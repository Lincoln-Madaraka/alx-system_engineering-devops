#!/usr/bin/python3
'''Module for task 2'''
import requests


def recurse(subreddit, hot_list=[], after=None):
    '''Return all hot post titles for a given subreddit'''
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Myscript/2.0 (by /u/kirlos)'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data').get('children')
        hot_list.extend(list(map(lambda x: x.get('data').get('title'), data)))
        after = response.json().get('data').get('after')
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None

