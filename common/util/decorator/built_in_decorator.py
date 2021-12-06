#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2021/11/24
---------------------------------------------------------------------
学习 python 内置的装饰器：
【 @classmethod 】
【 @staticmethod】

"""


class MethodDemo():
    def normal_method(self):
        print(" this is a normal method demo")

    # 定义类方法时候，必须添加 @classmethod 装饰器
    @classmethod
    def class_method(cls):
        """
        第一个参数 cls 是类本身, 相当于普通方法里的 self
        可以直接调用类内方法，类变量
        不可以调用实例方法和实例变量
        :return:
        """
        print("this is a class method demo ")

    @staticmethod
    def static_method():
        print(" this is a static method demo ")


# 定义分实例变量
method_demo = MethodDemo()

# classmethod 的调用
# 调用方式一：
MethodDemo.class_method()
# 调用方式二：
method_demo.class_method()

# staticmethod 的调用
MethodDemo.static_method()

# 普通方法的调用

method_demo.normal_method()
