#!/usr/bin/python3
"""Exports records of all employees tasks
and status in to a json file
"""
import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    todos = requests.get(url + "todos").json()

    with open("todo_all_employees.json", 'w') as jsonfile:
        record = {u['id']: [{"username": u["username"],
                             "task": t['title'],
                             "completed": t['completed']}
                            for t in todos if t['userId'] == u['id']]
                  for u in users}
        json.dump(record, jsonfile)
