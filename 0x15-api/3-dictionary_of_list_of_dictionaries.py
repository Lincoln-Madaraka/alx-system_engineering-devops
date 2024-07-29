#!/usr/bin/python3
'''Python script to export data in the json format'''
import json
import requests


def main():
    '''Entry point to the module'''
    todo_url = 'https://jsonplaceholder.typicode.com/todos/'
    user_url = 'https://jsonplaceholder.typicode.com/users/'
    json_file = 'todo_all_employees.json'
    user_json = requests.get(user_url).json()
    with open(json_file, 'w', encoding='utf8') as f:
        content = {}
        for i in range(len(user_json)):
            id = user_json[i]['id']
            username = user_json[i]['username']
            todo_json = requests.get(todo_url, params={'userId': id}).json()
            content[id] = []
            for i in range(len(todo_json)):
                content[id].append({'username': username,
                                    "task": todo_json[i]['title'],
                                    "completed": todo_json[i]['completed']})
        f.write(json.dumps(content))


if __name__ == '__main__':
    main()
