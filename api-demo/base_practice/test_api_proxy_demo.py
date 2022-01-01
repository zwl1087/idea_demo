#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2021/12/18

"""
import requests


class TestProxyDemo():

    def get_url(self):
        _get_url = "https://httpbin.testing-studio.com/get"
        return _get_url

    def post_url(self):
        _post_url = "https://httpbin.testing-studio.com/post"
        return _post_url

    def test_proxy_api(self):

        # 设置代理端口必须和 代理工具设置端口一致
        proxy = {
            # http 代理
            "http": "127.0.0.1:8888",
            # https 代理
            "https": "127.0.0.1:8888"
        }
        print(self.get_url())
        # 使用 proxies 参数开启代理
        # 使用 verify 屏蔽认证
        # 运行前必须先开启代理工具
        r = requests.get(self.get_url(), proxies = proxy, verify = False)
        print(r.json())
