#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2021/12/19

"""
import requests


class TestWorkWeixin():

    def test_get_access_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        param = {
            # 企业ID
            "corpid": "ww9dc9b0c15d8663a6",
            # 
            "corpsecret": "TomXTHsd_0naqWQYvRw5s-xNetlIWSHMiVkeAYDMDJk"
        }
        r = requests.get(url, params = param)
        print(r.url)
        print(r.text)
        access_token = r.json()["access_token"]
        print(r.json()["expires_in"])
        print(access_token)


