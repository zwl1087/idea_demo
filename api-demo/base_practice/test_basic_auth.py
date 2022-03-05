#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2021/12/19

"""
import requests
from requests.auth import HTTPBasicAuth


class TestBasicAuth():

    def get_url(cls):
        cls._get_url = "https://httpbin.testing-studio.com/basic-auth/banan/1234"
        return cls._get_url

    def test_basic_auth(self):
        proxy = {
            "http": "127.0.0.1:8888",
            "https": "127.0.0.1:8888"
        }
        print(self.get_url())
        auth = HTTPBasicAuth("banana", "1234")
        r = requests.get(self.get_url(), proxies = proxy, verify = False, auth = auth)
        print(r.request.headers['Authorization'])
        print(r.status_code)
