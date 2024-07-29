#!/usr/bin/python3
'''Python script to export data in the json format'''
import json
import requests
import sys


def main():
    '''Entry point to the module'''
    todo_url = 'https://jsonplaceholder.typicode.com/todos/'
    user_url = 'https://jsonplaceholder.typicode.com/users/'
    id = sys.argv[1]
    json_file = f'{id}.json'
    todo_json = requests.get(todo_url, params={'userId': id}).json()
    user_json = requests.get(user_url + id).json()
    username = user_json["username"]
    with open(json_file, 'w', encoding='utf8') as f:
        content = {id: []}

        for i in range(len(todo_json)):
            content[id].append({"task": todo_json[i]['title'],
                                "completed": todo_json[i]['completed'],
                                'username': username})
        f.write(json.dumps(content))


if __name__ == '__main__':
    main()
