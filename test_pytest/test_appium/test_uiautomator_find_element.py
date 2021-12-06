#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2021/11/28

"""
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


class TestFindElement():

    def setup(self):
        desire_cap = {
            "platformName": "Android",
            "platformVersion": "6.0",
            "deviceName": "emulator-5554",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "skipDeviceInitialization": True,
            "unicodeKeyboard": True,
            "resetKeyboard": True,
            "noReset": True  # Don't reset app state before this session. See here for more details
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(15)

    def teardown(self):
        # 返回上一页
        # self.driver.back()
        self.driver.quit()

    @pytest.mark.skip
    def test_login_my_xueqiu(self):
        # 点击”我的“
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        # 点击登录
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码")').click()
        # 输入账号密码
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("123456")
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("123456")
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()

    @pytest.mark.skip
    def test_multiple_conditions(self):
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("我的")').click()

    @pytest.mark.skip
    def test_child_selector(self):
        self.driver.find_element(By.ID, "com.xueqiu.android:id/tv_search").click()
        el1 = self.driver.find_element(By.ID, "com.xueqiu.android:id/search_input_text")
        el1.click()
        el1.send_keys("阿里巴巴")
        self.driver.find_element(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()

        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/title_container").childSelector(text("股票"))').click()

    def test_scroll_find_element(self):
        sleep(5)
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("梁剑").instance(0));').click()



