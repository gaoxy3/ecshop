import pytest
version=6
@pytest.mark.run(order=2)
class TestDept():
    @pytest.mark.parametrize("id,name",[(2,"aa"),(3,"ds"),(4,"we")])
    def test_add(self,id,name):
        print("添加部门",id,name)
    @pytest.mark.skipif(version>5,reason="版本大于5不需要执行该用例")
    def test_del(self):
        print("删除部门")
    def setup(self):
        print("在每个测试方法执行之前调用")
    def teardown(self):
        print("在每个测试方法执行之后调用")
    def setup_class(self):
        print("测试类刚开始调用一次")
    def teardown_class(self):
        print("测试类结束后调用一次")