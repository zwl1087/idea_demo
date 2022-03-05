#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2021/12/19

"""
from hamcrest import *
import requests
from jsonpath import jsonpath

"""
行业断言规范
使用 PyHamcrest 进行复杂结果的断言
"""


class demo_a():
    arr_a = [1, 2, 3]
    arr_b = [1, 2, 3]


class TestHamcrestAssert():

    # 断言相等
    def test_hamcrest_equal_to(self):
        r = requests.get("https://ceshiren.com/categories.json")
        # 打印 file 的内容
        print(r.text)
        # 使用jsonpath 表达式再 json 中查找节点
        print(jsonpath(r.json(), "$..name"))
        # 使用 assert_that("实际结果", equal_to("预期结果") ) equal_to 断言相等
        assert_that(jsonpath(r.json(), "$..name")[0], equal_to("开源项目"))

    def test_assert_array(self):
        da = demo_a()
        db = demo_a()
        assert_that(da, same_instance(db))
