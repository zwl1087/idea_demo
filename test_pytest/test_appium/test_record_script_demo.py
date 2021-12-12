#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2021/11/27

"""
from appium import webdriver
from selenium.webdriver.common.by import By

desire_cap = {
    "platformName": "Android",
    "platformVersion": "6.0",
    "deviceName": "emulator-5554",
    "appPackage": "com.xueqiu.android",
    "appActivity": ".view.WelcomeActivityAlias",
    "noReset": True     # Don't reset app-demo state before this session. See here for more details
}

# 配置 appium server 监听的端口
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
driver.implicitly_wait(10)

el0 = driver.find_element(By.ID, "com.xueqiu.android:id/tv_search").click()

el1 = driver.find_element(By.ID, "com.xueqiu.android:id/search_input_text")
el1.click()
el1.send_keys("ailibaba")

el2 = driver.find_element(By.ID, "com.xueqiu.android:id/name")
el2.click()
# 返回上一页
driver.back()
driver.back()
