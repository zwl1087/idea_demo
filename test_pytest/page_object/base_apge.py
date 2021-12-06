#!/usr/bin/python3
'''
author = zhaowenlong
project = pytestProject
date = 2021/11/21
'''
import logging
import yaml
from time import sleep
from selenium import webdriver

class BasePage:
    # 子类如果和父类的类属性重名，那么子类在实例化过程中会覆盖父类的类属性
    _base_url = None
    def __init__(self, driver = None):
        # 问题：子类没有构造函数时候，就会自动调用父类的构造函数, 因此会打开多个浏览器
        # 问题：如何避免driver 的重复实例化: 【添加 driver 参数 】
        """
        告诉父类的构造函数，如果传参了，不需要进行重复的实例化操作
        如果没有传参， 那么就是第一次的实例化操作，需要进行实例化
        :param driver:
        """
        # 如果base_driver 为真， 为真就是不等于None，那么就不需要重复实例化的操作
        if driver:
            # 非第一次实例化操作
            # 为了保证，后面的子类在使用的过程中，都具有driver属性，所以需要做赋值操作
            self.driver = driver
        # 如果base_driver 为None/假， 那么就需要对Driver进行实例化
        else:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(3)
            self.driver.maximize_window()
            self.driver.get(self._base_url)
            # 2、打开保存cookies的文件
            cookies = yaml.safe_load(open("../data/cookies.yaml"))
            for cookie in cookies:
                # 3、 添加cookies
                self.driver.add_cookie(cookie)
            sleep(3)
            # 4、添加cookies后重新登录页面
            self.driver.get(self._base_url)
            # 5、验证登录成功
            sleep(5)

    # 关键字封装思想
    def find(self, by, locator = None):
        if locator:
            res = self.driver.find_element(by, locator)
        else:
            res = self.driver.find_element(*by)
        return res

    def finds(self, by, locator = None):
        if locator:
            res = self.driver.find_elements(by, locator)
        else:
            # 元组解包操作： xxx((1, 2)) -> xxx(*(1,2))->xxx(1,2)
            res = self.driver.find_elements(*by)
        return res

    # 日志模块封装
    def add_log(self, log_level, log_content):
        if log_level == "info":
            logging.info(log_content)
        elif log_level == "debug":
            logging.debug(log_content)
        elif log_level == "warning":
            logging.warning(log_level)
        elif log_level == "error":
            logging.error(log_content)
        else:
            logging.error("LoggingLevelError: BasePage ADD_LOG ERROR  Logging Param ERROR ")
            raise Exception("LoggingLevelError")

