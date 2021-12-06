#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2021/11/27

"""

"""
主要介绍 app 元素的定位的三种方式
id、xpath、accessibility_id
"""

from appium import webdriver
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
            "noReset": True  # Don't reset app state before this session. See here for more details
        }

        # 配置 appium server 监听的端口
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):
        # 返回上一页
        self.driver.back()
        self.driver.back()

        self.driver.quit()


    @pytest.mark.skip
    def test_by_id(self):
        print("测试 by_id 开始")
        self.driver.find_element(By.ID, "com.xueqiu.android:id/tv_search").click()
        el1 = self.driver.find_element(By.ID, "com.xueqiu.android:id/search_input_text")
        el1.click()
        el1.send_keys("阿里巴巴")

        # 根据ID等位元素
        self.driver.find_element(By.ID, "com.xueqiu.android:id/name").click()
        el2 = self.driver.find_element(By.ID, "com.xueqiu.android:id/current_price")
        res_num = float(el2.text)
        print(f"阿里巴巴当前的股价为：{res_num}")

        assert res_num < 200

    def test_by_xpath(self):
        print("测试 by_xpath 开始")
        self.driver.find_element(By.ID, "com.xueqiu.android:id/tv_search").click()
        el1 = self.driver.find_element(By.ID, "com.xueqiu.android:id/search_input_text")
        el1.click()
        el1.send_keys("阿里巴巴")
        # 根据xpath 等位元素
        self.driver.find_element(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()

        el2 = self.driver.find_element(By.ID, "com.xueqiu.android:id/current_price")

        res_num = float(el2.text)
        print(f"阿里巴巴当前的股价为：{res_num}")

        assert res_num < 200


