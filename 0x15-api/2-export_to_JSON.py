#!/usr/bin/python3
"""Exports records of employee with each task
to a json file
"""
import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    with open("{}.json".format(sys.argv[1]), "w") as jsonfile:
        record = {sys.argv[1]: [{"task": t["title"],
                                 "completed": t["completed"],
                                 "username": user["username"]}
                                for t in todos]}
        json.dump(record, jsonfile)
