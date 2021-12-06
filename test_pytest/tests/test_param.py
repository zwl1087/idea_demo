import pytest
'''
pytest 的参数化框架：@pytest.mark.parametrize("name", search_coll_1)
"name" 必须和测试用例的参数名称一致
search_coll_1 中有多个值，会生成多条测试用例
'''


# 单个参数化
search_coll_1 = ["baidu", "webtest", "apptest"]
@pytest.mark.parametrize("name", search_coll_1)
def test_search_single(name):
    assert name in search_coll_1

# 多个参数
# 多个参数写在parametrize 的第一个参数的位置，并且用逗号分割
# 参数化的名字，与方法的的参数必须一致，且一一对应
# 测试变量写在第二个参数位置，传入list，并且嵌套元组
# 有多组测试变量的时候，每一组变量放在一个元组中
@pytest.mark.parametrize("test_input,expected",[("2*3",6),("4*5",20),("3+4",7)])
def test_search_more_1(test_input,expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize("test_input,expected",[("2*3",6)])
def test_search_more_2(test_input,expected):
    assert eval(test_input) == expected

# 测试用例重命名
# 使用parametrize 的ids参数
# ids的参数必须放在列表中，传递个数必须和变量参数一致
@pytest.mark.parametrize("test_input,expected",[("2*3",6),("4*5",20),("3+4",7)],
                         ids=["NO.test_demo_001","NO.test_demo_002","NO.test_demo_003"])
def test_search_more_1(test_input,expected):
    assert eval(test_input) == expected


# 笛卡尔积 : 两个集合的全排列组合集

@pytest.mark.parametrize("name",["webtset","apptest","apitest"])
@pytest.mark.parametrize("code",["utf-8","gbk","gb3213"])
def test_cartesian_product(name,code):
    print(f"name: {name},code :{code}")



