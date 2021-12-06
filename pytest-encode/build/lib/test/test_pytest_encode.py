import pytest

@pytest.mark.parametrize("name",["奶赵赵","小脑斧","小小脑斧"],ids=[f"No.测试用例_001","No.测试用例_002","No.测试用例_003"])
def test_case_name_cn(name):
    print(f"name:{name}")
