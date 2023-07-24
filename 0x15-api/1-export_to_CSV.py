#!/usr/bin/python3
"""For a given employee ID, returns information
about his/her TODO list progress
"""
import requests
import sys
import csv


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    with open("{}.csv".format(sys.argv[1]), 'w') as f:
        obj = csv.writer(f)
        [obj.writerow([user['id'], user['name'], t['completed'], t['title']])for t in todos]
