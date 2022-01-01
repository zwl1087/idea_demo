#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2021/12/20
"""

from jsonschema import validate
import requests
import json


# class TestJsonSchema:
#
#     def test_json_schema_assert(self):
#         r = requests.get("https://ceshiren.com/categories.json", params = {"limit": "2"})
#         print(r.status_code)
#         print(r.json())
#         schema = json.load(open("jsonschema.json"))
#         validate(r.json().encode("utf-8"), schema = schema)


def test_get_login_jsonschema():
    url = "https://ceshiren.com/categories.json"
    data = requests.get(url, params = {"limit":"2"}).json()
    print(data)
    # with open("jsonschema.json", encoding = 'utf8') as f:
    #     schema = json.load(f)
    schema = json.load(open("jsonschema.json",encoding = "utf-8"))
    validate(data, schema = schema)



