import requests
r = requests.request("post","http://47.92.229.35/jiekou/mobile/index.php?act=login",data={
    "username":"zhangsan",
    "password":"123456",
    "client":"android"
})
r.encoding=r.apparent_encoding
print(r.status_code)
print(r.text)
print(r.json())
print(r.url)
print(r.encoding)
print(r.apparent_encoding)
print(r.headers)
print(r.cookies)
r = requests.post("http://47.92.229.35/jiekou/mobile/index.php?act=login",data={
    "username":"zhangsan",
    "password":"123456",
    "client":"android"
})
print(r.json())
# r = requests.get("http://47.92.229.35/jiekou/mobile/index.php?act=goods_class")
r = requests.get("http://47.92.229.35/jiekou/mobile/index.php",params={
    "act":"goods_class"
})
print(r.json())