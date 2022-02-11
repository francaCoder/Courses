# Introduction
#services made available online to access features or functionality of any web application

# 4 Parts
# 1 - Url base
# 2 - Endpoint -  After URL
# 3 - Resource -  Everything that is returned or sent to an api
# 4 - Verbs HTTP - get (get existing data), post (send data), put (update/change data), delete

# Status codes
# 1xx: Information
# 2xx: Success
# 3xx: Redirection
# 4xx: Client ERROR
# 5xx: Server ERROR

import requests
from pprint import pprint

# get
# get_result = requests.get("https://jsonplaceholder.typicode.com/todos")
# pprint(get_result.json())

# Get with ID

# get_result_id2 = requests.get("https://jsonplaceholder.typicode.com/todos/2")
# pprint(get_result_id2.json())

# Post - New resource

new_task = {'completed': False,
 "title": "Wash the car",
 'userId': 1}

post_result = requests.post("https://jsonplaceholder.typicode.com/todos", new_task)
pprint(post_result.json())

# Put - Change a resource
change_task = {'completed': False,
 "title": "Wash the motorcycle",
 'userId': 1}
put_result = requests.put("https://jsonplaceholder.typicode.com/todos/2", change_task)
pprint(put_result.json())


# Delete

delete_result = requests.delete("https://jsonplaceholder.typicode.com/todos/2")
pprint(delete_result.json())