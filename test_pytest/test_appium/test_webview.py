#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2021/12/4

"""
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from appium import webdriver
"""
1、介绍webview 测试demo

"""



class TestBrowsers():

    def setup(self):
        desire_cap = {
            "platformName": "Android",
            "platformVersion": "6.0",
            # 1、指定浏览器的名称
            "browserName": "Browser",
            "deviceName": "emulator-5554",
            # 2、webview测试不需要指定 appPackage、appActivity
            # "appPackage": "com.xueqiu.android",
            # "appActivity": ".view.WelcomeActivityAlias",
            # 3、指定chromedriver的路径，否则使用默认路径
            "chromedriverExecutable": "D:\webdirver\chromedriver66\chromedriver.exe",
            "unicodeKeyboard": True,
            "resetKeyboard": True,
            "noReset": True  # Don't reset app state before this session. See here for more details
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):
        # 返回上一页
        # self.driver.back()
        self.driver.quit()

    def test_browser(self):
        self.driver.get("https://m.baidu.com")
        sleep(2)
        self.driver.find_element(By.ID, "index-form").click()
        self.driver.find_element(By.ID, "index-kw").send_keys("赵文龙")
        # 4、添加显示等待
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.ID, "index-bn")))
        self.driver.find_element(By.ID, "index-bn").click()
        sleep(5)

