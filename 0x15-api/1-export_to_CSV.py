#!/usr/bin/python3
""" Script that exports employee information to CSV"""

if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    employee_ID = int(argv[1])
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(employee_ID))
    employee_name = r.json().get('username')
    r = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                     .format(employee_ID))
    tasks = r.json()

    file_name = "{}.csv".format(employee_ID)
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(["USER_ID", "USERNAME",
                         "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in tasks:
            task_title = task["title"]
            task_completed = task["completed"]
            writer.writerow([employee_ID, employee_name,
                             task_completed, task_title])
