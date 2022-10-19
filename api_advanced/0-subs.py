#!/usr/bin/python3
""" Return the number of subsribers """
import requests


def number_of_subscribers(subreddit):
    """ Return the numbers of subscribers """
    base_url = 'https://www.reddit.com'
    api_one = '{base}/r/{subreddit}/about.json'.format(base=base_url,
                                                       subreddit=subreddit)
    user_agent = {'User-Agent': 'Python/requests'}
    res = requests.get(api_one, headers=user_agent,
                       allow_redirects=False)
    if res.status_code in [302, 404]:
        return 0
    return res.json().get('data').get('subscribers')
