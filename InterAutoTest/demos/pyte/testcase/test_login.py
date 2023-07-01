import pytest
@pytest.mark.run(order=1)
class TestLogin():
    @pytest.mark.parametrize("name",["张三","李四"])
    def test_login(self,name):
        print("登录",name)
    @pytest.mark.skip()
    def test_login1(self):
        print("登录2")