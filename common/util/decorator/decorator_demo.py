#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2021/11/24

"""

# 定义一个装饰器
from time import sleep
import datetime

def timer(func):
    def inner(*args, **kwargs):

        start_time = datetime.datetime.now()
        print(f" *** 函数开始执行, 计时开始: {start_time}")
        func(*args, **kwargs)
        end_time = datetime.datetime.now()
        print(f" *** 函数执行结束, 计时结束: {end_time}")
        print(f"函数执行的时间是： {end_time - start_time}")

    return inner

# 调用装饰器
@timer
# 定义一个可执行函数
def hogwarts(name, age, gender):
    print(f"霍格沃兹测试学院:  学员姓名：{name}, 学员年龄：{age}, 学员性别{gender}")
    sleep(3)


# 调用使用了装饰器定义的函数
hogwarts("zhangsan", 12, "man")


# 执行结果：
"""
E:\pytestProject\venv\Scripts\python.exe E:/pytestProject/util/python_basics/decorator_demo.py
 *** 函数开始执行, 计时开始: 2021-11-24 23:04:03.370588
霍格沃兹测试学院:  学员姓名：zhangsan, 学员年龄：12, 学员性别man
 *** 函数执行结束, 计时结束: 2021-11-24 23:04:06.384423
函数执行的时间是： 0:00:03.013835

Process finished with exit code 0
"""

