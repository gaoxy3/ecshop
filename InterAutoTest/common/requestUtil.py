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