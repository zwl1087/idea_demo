#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2021/12/18

"""
import allure
import requests

"""
requests 编写测试用例
接口请求构造
"""


class TestBaseDemo:

    # 构造简单的 get 请求：【 requests.get(url) 】
    @allure.title("构造简单的get请求")
    @allure.story("base request")
    def test_get(self):
        r = requests.get("https://httpbin.testing-studio.com/get")
        print(r.text)
        assert r.status_code == 200

    # 构造简单的post请求：【 requests.post(url) 】
    @allure.title("构造简单的post请求")
    @allure.story("base request")
    def test_post(self):
        r = requests.post("https://httpbin.testing-studio.com/post")
        print(r.text)
        assert r.status_code == 200

    # 构造带有 params 的 get 请求: 【 requests.get(url, params = payload) 】
    @allure.title("构造带有params的get请求")
    @allure.story("params")
    def test_get_param(self):
        payload = {
            "level": 1,
            "name": "hogwz-zwl-params"
        }
        r = requests.get("https://httpbin.testing-studio.com/get", params = payload)
        # 打印 params 的内容
        print(r.json()["args"])
        # 带参数最终发起请求的URL
        print("带参数最终发起请求的URL", r.json()["url"])
        # 添加多条断言
        assert r.status_code == 200  # 断言状态码
        assert r.json()["args"]["name"] == "hogwz-zwl-params"  # 断言 params 的内容

    # 构造一个简单的 form 请求： 【 requests.post(url,  data= data) 】
    # 模拟用户名密码等表单输入
    @allure.title("构造一个简单的form请求")
    @allure.story("form")
    def test_post_form(self):
        data = {
            "level": 1,
            "name": "hogwz-zwl-form"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", data = data)
        # print(r.text)
        # 打印 form 的内容
        print("form 的内容", r.json()["form"])
        assert r.status_code == 200
        assert r.json()["form"]["name"] == "hogwz-zwl-form"

    # 构造 files 请求： 【 requests.post(url, files = open(filepath, "rb")) 】
    @allure.title("构造files请求")
    @allure.story("files")
    def test_post_file(self):
        data = {
            "level": 1,
            "name": "hogwz-zwl-files"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", files = data)
        # print(r.text)
        # 打印 file 的内容
        print("files 的内容是：  ", r.json()["files"])
        print(r.headers)
        assert r.status_code == 200
        assert r.json()["files"]["name"] == "hogwz-zwl-files"

    @allure.title("构造json data的post请求")
    @allure.story("application/json")
    def test_post_json(self):
        data = {
            "level": 1,
            "name": "hogwz-zwl-json"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", json = data)
        print(r.json()["data"])
        # 打印 file 的内容
        print("json 的内容是：  ", r.json()["json"])
        print(r.headers)
        assert r.status_code == 200
        assert r.json()["json"]["name"] == "hogwz-zwl-json"
        assert r.headers["Content-Type"] == 'application/json'

    @allure.title("构造xml data的post请求")
    @allure.story("application/xml")
    def test_post_xml(self):
        xml = """<?xml version='1.0' encoding='utf-8'?>
                <languge>
                    <option> C </option>
                    <option> C++ </option>
                    <option> Java </option>
                    <option> Python </option>
                    <option> JavaScript </option>
                </languge>"""
        header = {"content-type": "application/xml"}
        r = requests.post("https://httpbin.testing-studio.com/post", headers = header, data = xml)
        print(r.text)

    # 构造请求的header： 【 requests.post(url, headers= header) 】
    @allure.title("构造请求的header")
    @allure.story("headers")
    def test_request_headers(self):
        header = {
            "level": "1",
            "name": "hogwz-zwl"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", headers = header)

        # 打印 header 的内容
        # print(r.json())
        print(r.json()["headers"])
        assert r.status_code == 200
        assert r.json()["headers"]["Name"] == "hogwz-zwl"

    # 在请求头中构造 cookies: header
    @allure.title("在请求头中构造 cookies")
    @allure.story("Cookies")
    def test_request_cookies_by_header(self):
        # header 传递Cookie时，首字母必须大写，否则不能被识别到
        header = {
            "Cookie": "header-cookies-demo"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", headers = header)

        print(r.json()['headers']['Cookie'])
        assert r.json()['headers']['Cookie'] == 'header-cookies-demo'

    # 使用cookies构造cookies: cookies
    @allure.title("使用cookies构造cookies")
    @allure.story("Cookies")
    def test_request_cookies_by_cookies(self):
        cookies = dict(cookies_demo = "my cookies", cookies_token = "my token")
        r = requests.post("https://httpbin.testing-studio.com/post", cookies = cookies)

        print(r.json()["headers"]["Cookie"])
        assert r.json()["headers"]["Cookie"] == "cookies_demo=my cookies; cookies_token=my token"
