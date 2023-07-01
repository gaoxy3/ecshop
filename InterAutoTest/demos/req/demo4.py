import requests
class Request():
    def request(self,url,method="GET",token=None,**kwargs):
        if token:
            headers = kwargs.get("headers",{})
            headers["Authorization"] = token
            kwargs["headers"] = headers
        r = requests.request(method,url,**kwargs)
        try:
            data=r.json()
        except:
            data = r.text
        return data
    def get(self,url,token=None,**kwargs):
        return self.request(url,token=token,**kwargs)
    def post(self,url,token=None,**kwargs):
        return self.request(url,method="POST",token=token,**kwargs)

if __name__ == '__main__':
    r=Request().post("http://127.0.0.1:5000/api/login",data={
        "username":"孙华",
        "password":"123456"
    })
    print(r)
    token = r["data"]["token"]
    print(token)
    r=Request().request("http://127.0.0.1:5000/api/addDept",method="POST",data={
        "deptname":"销售部"
    },token=token)
    print(r)
