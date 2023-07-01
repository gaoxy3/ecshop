from common.requestUtil import Request

def getToken(url,params):
    res=Request().post(url,data=params)
    return res["data"]["token"]


if __name__ == '__main__':
    print(getToken("http://127.0.0.1:5000/api/login",{
        "username":"孙华",
        "password":"123456"
    }))