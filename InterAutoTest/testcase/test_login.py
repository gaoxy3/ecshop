import pytest,json,allure
from common.requestUtil import Request
from common.excelUtill import ExcelUtill
from common.logUtill import LogUtill
log = LogUtill().logger
@pytest.mark.run(order=1)
@allure.feature("登录模块")
class TestLogin():
    @pytest.mark.parametrize("url,datas,title",ExcelUtill("data/接口测试用例.xlsx").getDatas([3,5,2]))
    @allure.story("登录-二级标题")
    # @allure.title("登录")
    @allure.description("用户登录接口，需要用户名和密码")
    def test_login(self,url,datas,title):
        allure.dynamic.title(title)
        res = Request().post(url,data=json.loads(datas))
        log.info("接口:"+url+"参数:"+datas)
        print(res)
    @pytest.mark.skip()
    @allure.story("登录-二级标题")
    @allure.title("登录2")
    def test_login1(self):
        print("登录2")

    @allure.story("注销-二级标题")
    @allure.title("注销")
    @allure.severity("critical")
    def test_logout(self):
        print("注销")