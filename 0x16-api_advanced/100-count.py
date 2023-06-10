#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit"""

import requests


def count_words(subreddit, word_list, count_dict=None, after=None):
    if count_dict is None:
        count_dict = {}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {
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
        headers=headers,
        params=params,
        allow_redirects=False
    )
    if response.status_code == 200:
        body = response.json()
        children = body['data']['children']

        for child in children:
            title = child['data']['title'].lower()
            for word in word_list:
                if word.lower() in title.lower() and \
                   not title.endswith(('.', '!', '_')):
                    count_dict[word.lower()] = (
                        count_dict.get(word.lower(), 0) + 1)

        after = body['data']['after']
        if after is not None:
            return count_words(subreddit, word_list, count_dict, after=after)

    sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")
