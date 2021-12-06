# import pytest
#
# # 作用域，当前目录和 其所有的子目录生效，
# # 父目录不生效
#
#
# # 定义 fixture
# @pytest.fixture(autouse=True)
# def open_browser():
#     print("open browser")
# @pytest.fixture()
# def connet_db():
#     print("db had been conneted")
# # session 级别的fixture ，作用在整个项目中 pytest 命令下的所有：
# # 在整个项目下执行一次
# @pytest.fixture(scope="session")
# def start_test_func():
#     print(" test starting now ")
#
#
# @pytest.fixture(autouse=True)
# def stat_test_flag():
#     print("【开始计算】")
#
#
# @pytest.fixture(autouse=True)
# def end_test_flag():
#     print("【结束计算】")
#
# @pytest.fixture(scope="moudle",autouse=True)
# def end_test_case():
#     print("【测试结束】")
#
