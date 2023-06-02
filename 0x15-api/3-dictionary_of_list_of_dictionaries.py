#!/usr/bin/python3
"""script to save & export data in JSON format"""

if __name__ == "__main__":
    import json
    import requests

    r = requests.get('https://jsonplaceholder.typicode.com/users')
    users = r.json()

    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = r.json()

    export_data = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        user_tasks = [task for task in tasks if task.get('userId') == user_id]
        export_data[user_id] = [{
            'username': username,
            'task': task.get('title'),
            'completed': task.get('completed')
        } for task in user_tasks]

    filename = 'todo_all_employees.json'
    with open(filename, 'w') as f:
        json.dump(export_data, f)
