import requests
import json

URL = 'http://127.0.0.1:8000/rest_api/'

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    data = r.json()
    print(data)
get_data()

def post_data():
    data = {
        "name" : "vikas",
        'roll' : 122,
        'age' : 23,
 }
    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data)
    data = r.json()
    print(data)
# post_data()

def update_data():
    data = {
        "id": 14,
        "name" :" deepak"
 }
    json_data = json.dumps(data)
    r = requests.put(url = URL, data = json_data)
    data = r.json()
    print(data)
# update_data()

def delete_data():
    data = {
        "id": 13,
    }
    json_data = json.dumps(data)
    r = requests.delete(url = URL, data = json_data)
    data = r.json()
    print(data)
# delete_data()
    
    

# URL = 'http://127.0.0.1:8000/user_create/'
# data = {
#     'name' :'gyan',
#     'age' : 14,
#     'roll' : 50,
# }
# json_data = json.dumps(data)

# r  = requests.post(url = URL, data = json_data)

# data = r.json()
# print(data)