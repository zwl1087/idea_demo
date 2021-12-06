#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2021/11/28

"""
"""
获取元素的属性值
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
        # self.driver.back()

        self.driver.quit()

    def test_get_element_attribute(self):
        # 定位搜素框
        global res_element_enable
        search_ele = self.driver.find_element(By.ID, "com.xueqiu.android:id/tv_search")
        # 获取name属性值
        print(search_ele.get_attribute("name"))
        # 获取 text属性值
        print("text: ", search_ele.text)
        # 获取位置属性值
        print("location: ", search_ele.location)
        # 获取控件大小属性值
        print("size", search_ele.size)

        # 控件是否可用
        if search_ele.is_enabled():
            search_ele.click()
            self.driver.find_element(By.ID, "com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")

            res_element = self.driver.find_element(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            # 控件是否可见
            res_element_enable = res_element.is_displayed()

            if res_element_enable :
                print("res_element搜素结果：",res_element_enable)
            else:
                print("res_element搜素失败")
        else:
            print("search_ele 搜索框不可用")
        assert res_element_enable







