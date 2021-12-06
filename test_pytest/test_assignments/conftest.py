# import pytest
# import logging
# import datetime
# import time
# from func.operation import Caclultor
#
# filename = time.strftime("%Y-%m-%d-%H",time.localtime(time.time()))
#
# logging.basicConfig(level = logging.INFO,
#                     format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     filename=filename,filemode='a')
# logger = logging.getLogger(__name__)
#
#
#
# # @pytest.fixture()
# # def get_cale():
# #     calc = Caclultor()
# #     return calc
#
#
#
#
# @pytest.fixture()
# def log_record(content):
#     logging.info(content)
#
# # 使用 fixture 定义 calc 对象
# @pytest.fixture(scope="session", autouse=True)
# def get_calc():
#     calc = Caclultor()
#     yield calc
#     print("【测试结束】")
#
# @pytest.fixture(autouse=True)
# def print_log():
#     print("开始计算")
#     yield
#     print("结束计算")
#
