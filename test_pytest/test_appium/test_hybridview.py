#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2021/12/5

"""
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from appium import webdriver

"""
1、介绍 hybrid view 测试demo

"""


class TestBrowsers():

    def setup(self):
        desire_cap = {
            "platformName": "Android",
            "platformVersion": "6.0",
            # 1、不再指定浏览器的名称
            # "browserName": "Browser",
            "deviceName": "emulator-5554",
            # 2、hybrid view 测试需要指定 appPackage、appActivity
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            # 3、指定chromedriver的路径，否则使用默认路径
            "chromedriverExecutable": "D:\webdirver\chromedriver66\chromedriver.exe",
            "unicodeKeyboard": True,
            "resetKeyboard": True,
            "noReset": True  # Don't reset app state before this session. See here for more details
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_hybird_view(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/tab_name" and @text="交易"]'). \
            click()
        print(self.driver.contexts)
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="app"]//*[@class="android.view.View" and '
                                                 '@text="去开户"]').click()
        sleep(2)
        # print(self.driver.page_source)
        print(self.driver.contexts)
        self.driver.switch_to.context(self.driver.contexts[-1])

        self.driver.find_element(By.ID, "phone-number").send_keys("13533441234")
        self.driver.find_element(By.ID, "code").send_keys("456123")
        self.driver.find_element(MobileBy.XPATH, '//*[@class="android.view.View" and @text="立即开户"]').click()

        sleep(3)
