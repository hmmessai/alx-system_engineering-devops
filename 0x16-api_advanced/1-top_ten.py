#!/usr/bin/python3
"""Queries reddit for a subreddit
and prints the titles of the first 10 hot posts
listed inside it
data.children.data.title
"""
import requests


def top_ten(subreddit):
    """Returns the titles of top 10 posts for a subreddit"""
    url = "https://www.reddit.com/r/{}/best.json".format(subreddit)

    response = requests.get(url, allow_redirects=False)
    if response.status_code == 404:
        print(None)
        return
    children = response.json().get("data")
    if children.get("children") is None:
        print(None)
        return
    i = 0
    while i < 10:
        for child in children.get("children"):
            print(child.get("data").get("title"))
        i += 1
