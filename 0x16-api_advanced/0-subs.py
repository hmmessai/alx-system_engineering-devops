#!/usr/bin/python3
"""Queries the reddit api and
return the nubmer of subscribers
for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers of the given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {
            "User-Agent": "Python-requests/2.25.1"
    }
    response = requests.get(url,  headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results["subscribers"]
