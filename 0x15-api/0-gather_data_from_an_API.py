#!/usr/bin/python3
'''Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress'''
import json
import requests
import sys


def main():
    '''Entry point to the module'''
    todo_url = 'https://jsonplaceholder.typicode.com/todos/'
    user_url = 'https://jsonplaceholder.typicode.com/users/'
    id = sys.argv[1]
    todo_responce = requests.get(todo_url, params={'userId': id})
    user_responce = requests.get(user_url + id)
    user_json = json.loads(user_responce.text)
    todo_json = json.loads(todo_responce.text)
    user_name = user_json["name"]
    total_number_of_tasks = len(todo_json)
    number_of_done_tasks = 0
    for i in range(total_number_of_tasks):
        if todo_json[i]['completed']:
            number_of_done_tasks += 1
    print('Employee {} is done with tasks({}/{}):'.format(
        user_name, number_of_done_tasks, total_number_of_tasks
        ))
    for i in range(total_number_of_tasks):
        if todo_json[i]['completed']:
            print('\t ' + todo_json[i]['title'])


if __name__ == '__main__':
    main()

