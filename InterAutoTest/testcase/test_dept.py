import pytest,json,allure
from common.tokenUtill import getToken
from common.requestUtil import Request
from common.excelUtill import ExcelUtill
version=6
@pytest.mark.run(order=2)
@allure.feature("部门模块")
class TestDept():
    @pytest.mark.parametrize("url,datas",ExcelUtill("data/接口测试用例.xlsx",1).getDatas([3,5]))
    @allure.story("部门-二级标题")
    def test_add(self,url,datas):
        res=self.request.post(url,data=json.loads(datas),token=self.token)
        print(res)
    @pytest.mark.parametrize("url",ExcelUtill("data/接口测试用例.xlsx",2).getDatas([3]))
    @allure.story("部门-二级标题")
    @allure.severity(allure.severity_level.MINOR)
    def test_getAll(self,url):
        res=self.request.get(url,token=self.token)
        print(res)
    @pytest.mark.skipif(version>5,reason="版本大于5不需要执行该用例")
    @allure.story("部门-二级标题")
    def test_del(self):
        print("删除部门")
    # def setup(self):
    #     print("在每个测试方法执行之前调用")
    # def teardown(self):
    #     print("在每个测试方法执行之后调用")
    def setup_class(self):
        self.token=getToken("http://127.0.0.1:5000/api/login", {
            "username": "孙华",
            "password": "123456"
        })
        self.request=Request()
    # def teardown_class(self):
    #     print("测试类结束后调用一次")