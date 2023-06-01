#!/usr/bin/python3

""" Script that uses JSONPlaceholder API to get information about employee & exports to CSV"""
from sys import argv
import csv
import requests

def export_employee_todo_csv(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    employee_response = requests.get(employee_url)
    employee_response.raise_for_status()
    employee_data = employee_response.json()
    employee_name = employee_data["username"]

    todo_response = requests.get(todo_url)
    todo_response.raise_for_status()
    todo_data = todo_response.json()

    file_name = f"{employee_id}.csv"
    with open(file_name, mode='w', newline='') as file:
        writer  = csv.writer(file, quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todo_data:
            task_title = task["title"]
            task_completed = task["completed"]
            writer.writerow([employee_id, employee_name, task_completed, task_title])

    print(f"Exported tasks for employee {employee_name} to {file_name} successfully.")

"""
def display_csv_content(file_name):
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
"""

if __name__ == "__main__":
    employee_id = int(argv[1])
    export_employee_todo_csv(employee_id)
"""
    file_name = f"{employee_id}.csv"
    display_csv_content(file_name)
"""
