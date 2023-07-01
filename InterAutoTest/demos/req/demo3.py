import requests
r = requests.post("http://127.0.0.1:5000/api/login",data={
    "username":"孙华",
    "password":"123456"
})
print(r.json())
token = r.json()["data"]["token"]
print(token)
r = requests.post("http://127.0.0.1:5000/api/addDept",data={
    "deptname":"实施部"
},headers={
    "Authorization":token
})
print(r.json())