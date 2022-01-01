#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2021/12/19

"""
import requests

from jsonpath import jsonpath

from requests_xml import XMLSession

"""
1、 针对json响应结果的断言
2、 正对xml响应结果的断言
"""


class TestAssertResponse():

    def test_json_assert(self):
        r = requests.get("https://ceshiren.com/categories.json")

        # 打印 file 的内容
        print(r.text)
        # 使用jsonpath 表达式再 json 中查找节点
        print(jsonpath(r.json(), "$..name"))
        # 根据 jsonpath 表达式查询的结果进行断言
        assert jsonpath(r.json(), "$..name")[0] == "开源项目"

    def test_xml_assert(self):

        # 发起一个 xml 请求
        session = XMLSession()
        r = session.get("https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss")
        # 通过 xpath 路径定位结果节点
        item = r.xml.xpath("//item[1]/title", first= True)
        print(item.text)


