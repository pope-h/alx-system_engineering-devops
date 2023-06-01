#!/usr/bin/python3
"""
Script that uses JSONPlaceholder API to get information about an employee
"""

import requests
from sys import argv


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    employee_response = requests.get(employee_url)
    employee_response.raise_for_status()
    employee_data = employee_response.json()
    employee_name = employee_data["name"]

    todo_response = requests.get(todo_url)
    todo_response.raise_for_status()
    todo_data = todo_response.json()
    total_tasks = len(todo_data)
    done_tasks = sum(task["completed"] for task in todo_data)

    print("Employee", employee_name, "is done with tasks",
          "({}/{})".format(done_tasks, total_tasks) + ":")

    for task in todo_data:
        if task["completed"]:
            print(f"\t{task['title']}")


if __name__ == "__main__":
    employee_id = int(argv[1])
    get_employee_todo_progress(employee_id)
