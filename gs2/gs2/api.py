import requests
import json

URL = 'http://127.0.0.1:8000/studentapi/'

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    
    headers = {'content-Type':'application/json'} 
    json_data = json.dumps(data)
    r = requests.get(url = URL, headers = headers,data =json_data)
    data = r.json()
    print(data)
get_data(9)

def post_data():
    data = {
        "name" : "human",
        'roll' : 222, 
        'city' : "surat",
    }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url = URL, headers = headers, data = json_data)
    data = r.json()
    print(data)
# post_data()

def update_data():
    data = {
        "id": 1,
        "name" :" deepak"
 }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url = URL,headers = headers, data = json_data)
    data = r.json()
    print(data)
# update_data()

def delete_data():
    data = {
        "id": 1,
    }
    headers = {'content-Type':'application/json'}
    
    json_data = json.dumps(data)
    r = requests.delete(url = URL, headers = headers,data = json_data)
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