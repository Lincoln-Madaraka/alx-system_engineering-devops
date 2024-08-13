#!/usr/bin/python3
'''Module for task 100'''
import requests


def count_words(subreddit, word_list, hot_list=[], after=None):
    '''Count words in all hot posts titles of a subreddit'''
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
            return count_words(subreddit, word_list, hot_list, after)
        else:
            word_dict = {}
            for word in word_list:
                word_dict[word.lower()] = 0
            for title in hot_list:
                for word in title.split():
                    if word.lower() in word_dict:
                        word_dict[word.lower()] += 1
            for key in sorted(word_dict, key=word_dict.values(), reverse=True):
                if word_dict[key] > 0:
                    print('{}: {}'.format(key, word_dict[key]))
    else:
        return None
