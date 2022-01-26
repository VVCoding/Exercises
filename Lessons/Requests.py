# Author: Vedant Vohra
# Date:1/4/2022
# This is a lesson about Web API's

# API - Application Interface
# Client/Servers
# Request/Reply

# Information transfer is carried using JSON notation
# JSON - JavaScript Object Notation

import requests

api_url = 'https://jsonplaceholder.typicode.com/todos/1'
response = requests.get(api_url)

data = response.json()
print(response.json())
print(data['userId'])
