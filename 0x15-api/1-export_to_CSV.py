#!/usr/bin/python3
""" Script that exports employee information to CSV"""

if __name__ == "__main__":
    import requests
    from sys import argv

    employee_ID = int(argv[1])
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(employee_ID))
    employee_name = r.json().get('username')
    r = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                     .format(employee_ID))
    tasks = r.json()
    all_tasks = [item for item in tasks if item.get('userId') == employee_ID]

    file_name = "{}.csv".format(employee_ID)
    with open(file_name, mode='w+') as file:
        for task in all_tasks:
            file.write('"{}","{}","{}","{}"\n'.format(employee_ID,
                                                      employee_name,
                                                      task.get('completed'),
                                                      task.get('title')))
