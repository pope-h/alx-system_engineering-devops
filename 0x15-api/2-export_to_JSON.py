#!/usr/bin/python3
"""a script to save task information in JSON format"""

if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    employee_ID = argv[1]
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(employee_ID))
    employee_name = r.json().get('username')

    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = r.json()
    employee_tasks = [item for item in tasks if item.get('userId') ==
                      int(employee_ID)]

    export_data = {
        str(employee_ID): [{
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": employee_name
        } for task in employee_tasks]
    }

    file_name = "{}.json".format(employee_ID)
    with open(file_name, 'w') as f:
        json.dump(export_data, f)
