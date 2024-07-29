#!/usr/bin/python3
'''Python script to export data in the CSV format'''
import json
import requests
import sys


def main():
    '''Entry point to the module'''
    todo_url = 'https://jsonplaceholder.typicode.com/todos/'
    user_url = 'https://jsonplaceholder.typicode.com/users/'
    id = sys.argv[1]
    csv_file = f'{id}.csv'
    todo_responce = requests.get(todo_url, params={'userId': id})
    user_responce = requests.get(user_url + id)
    user_json = json.loads(user_responce.text)
    todo_json = json.loads(todo_responce.text)
    username = user_json["username"]
    total_number_of_tasks = len(todo_json)
    number_of_done_tasks = 0
    for i in range(total_number_of_tasks):
        if todo_json[i]['completed']:
            number_of_done_tasks += 1
    with open(csv_file, 'w', encoding='utf8') as f:
        for i in range(len(todo_json)):
            f.write('"{}","{}","{}","{}"\n'.format(
                id, username, todo_json[i]['completed'],
                todo_json[i]['title']))


if __name__ == '__main__':
    main()

