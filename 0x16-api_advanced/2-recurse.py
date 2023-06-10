#!/usr/bin/python3
'''
A module containing functions for working with the Reddit API.
'''

import requests


def recurse(subreddit, hot_list=[], after=None):
    '''
    Retrieves a list of hot posts from a given subreddit.
    '''
    url = f'https://www.reddit.com/r/{subreddit}.json?sort=hot'
    api_headers = {
        'Accept': 'application/json',
        'User-Agent': ' '.join([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'AppleWebKit/537.36 (KHTML, like Gecko)',
            'Chrome/97.0.4692.71',
            'Safari/537.36',
            'Edg/97.0.1072.62'
        ])
    }
    params = {'after': after} if after else {}
    response = requests.get(
        url,
        headers=api_headers,
        params=params,
        allow_redirects=False
    )
    if response.status_code == 200:
        jResponse = response.json()
        children = jResponse['data']['children']

        for child in children:
            hot_list.append(child['data']['title'])

        after = jResponse['data']['after']

        if after is not None:
            return recurse(subreddit, hot_list=hot_list, after=after)
        else:
            return hot_list

    else:
        return None
