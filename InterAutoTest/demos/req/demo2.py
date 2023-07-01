import requests

r = requests.post("http://47.92.229.35/jiekou/mobile/index.php?act=login",data={
    "username":"zhangsan",
    "password":"123456",
    "client":"android"
})
print(r.json())
key = r.json()["datas"]["key"]
r = requests.post("http://47.92.229.35/jiekou/mobile/index.php?act=logout",data={
    "key":key,
    "client":"android",
    "username":"zhangsan"
})
print(r.json())

