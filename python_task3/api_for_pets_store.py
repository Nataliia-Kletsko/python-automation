#Create_user
import requests
import json

url = "https://petstore.swagger.io/v2/user"

payload = json.dumps({
  "id": 0,
  "username": "Nata",
  "firstName": "Nataliia",
  "lastName": "Kletsko",
  "email": "nataliia.kletsko@gmail.com",
  "password": "RandomPassword@",
  "phone": "380671111111",
  "userStatus": 0
})
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'api_key': 'special-key'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

#Login_as_user
import requests

url = "https://petstore.swagger.io/v2/user/login?username=Nata&password=RandomPassword@"

payload = ""
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


#Create_list_of_user
import requests
import json

url = "https://petstore.swagger.io/v2/user/createWithList"

payload = json.dumps([
  {
    "id": 0,
    "username": "Nata",
    "firstName": "Nataliia",
    "lastName": "Kletsko",
    "email": "nataliia.kletsko@gmail.com",
    "password": "RandomPassword@",
    "phone": "380671111111",
    "userStatus": 0
  }
])
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api_key': 'special-key'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

#Log_out_user
import requests
import json

url = "https://petstore.swagger.io/v2/user/logout"

payload = {}
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

#Add_new_pet
import requests
import json

url = "https://petstore.swagger.io/v2/pet"

payload = json.dumps({
  "id": 0,
  "category": {
    "id": 0,
    "name": "My dog"
  },
  "name": "doggie",
  "photoUrls": [
    "https://upload.wikimedia.org/wikipedia/commons/4/43/Cute_dog.jpg"
  ],
  "tags": [
    {
      "id": 123,
      "name": "mydog"
    }
  ],
  "status": "available"
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

#Update_existing_pet
import requests
import json

url = "https://petstore.swagger.io/v2/pet"

payload = json.dumps({
  "id": 9223372036854774000,
  "category": {
    "id": 0,
    "name": "Beautiful Dog"
  },
  "name": "Beautiful Dog",
  "photoUrls": [
    "https://upload.wikimedia.org/wikipedia/commons/4/43/Cute_dog.jpg"
  ],
  "tags": [
    {
      "id": 123,
      "name": "mydog"
    }
  ],
  "status": "unavailable"
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)

#Delete_pet
import requests
import json

url = "https://petstore.swagger.io/v2/pet/9223372036854773724"

payload = {}
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)

