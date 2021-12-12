#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2021/12/12

"""
from appium.webdriver.webdriver import WebDriver

"""
页面基础操作，保存 driver、find、 etc;
"""


class BasePage:

    def __init__(self, driver: WebDriver = None):
        """

        :type driver: object
        """
        self.driver = driver
