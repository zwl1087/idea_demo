#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2021/11/28

"""
from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
import pytest


class TestFindElement():

    def setup(self):
        desire_cap = {
            "platformName": "Android",
            "platformVersion": "6.0",
            "deviceName": "emulator-5554",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",

            "unicodeKeyboard": True,
            "resetKeyboard": True,
            "noReset": True  # Don't reset app-demo state before this session. See here for more details
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):
        # 返回上一页
        # self.driver.back()
        self.driver.quit()

    def test_touch_actions(self):
        print("测试 touch_actions 开始")
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id = "com.xueqiu.android:id/title_text" and @text="推荐"]').click()

        size_dict = self.driver.get_window_rect()
        x_end = x_start = size_dict["width"] / 2
        y_start = size_dict["height"] * 0.8
        y_end = size_dict["height"] * 0.2
        # print(self.driver.get_window_rect())

        sleep(2)
        action = TouchAction(self.driver)
        print("开始滑动页面了")
        sleep(2)
        action.press(x = x_start, y = y_start).wait(3000).move_to(x = x_end, y = y_end).release().perform()
        print("页面滑动结束了")

