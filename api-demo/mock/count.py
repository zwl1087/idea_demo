#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2021/12/26

"""
from mitmproxy import ctx

num = 0


# flow 表示请求
def request(flow):
    # 函数内部使用外部变量时，需要用 global 参数
    global num
    num = num + 1
    ctx.log.info("共接收到 %d 个请求" % num)



