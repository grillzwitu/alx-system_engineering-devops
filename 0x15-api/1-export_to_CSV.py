#!/usr/bin/python3
"""
Uses the api https://jsonplaceholder.typicode.com with an employee ID to
return information about the employee's todo list progress, exports the
data as csv
"""

import csv
import requests
from sys import argv

if __name__ == '__main__':
    userId = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userId), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(userId), verify=False).json()
    with open("{}.csv".format(userId), 'w', newline='') as mycsvfile:
        taskwriter = csv.writer(mycsvfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            taskwriter.writerow([int(userId), user.get('username'),
                                 task.get('completed'),
                                 task.get('title')])
