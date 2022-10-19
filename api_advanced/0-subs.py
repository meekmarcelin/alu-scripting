#!/usr/bin/python3
""" Return the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ Return a number of subscribers """
    base_url = 'https://www.reddit.com'
    api_one = '{base}/r/{subreddit}/about.json'.format(base=base_url,
                                                       subreddit=subreddit)
    user_agent = {'User-Agent': 'Python/requests'}
    res = requests.get(api_uri, headers=user_agent,
                       allow_redirects=False)
    if res.status_code in [302, 404]:
        return 0
    return res.json().get('data').get('subscribers')
