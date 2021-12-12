#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2021/11/23

"""

from appium import webdriver


def test_first_appium_demo():
    desired_caps = {}
    # 平台的名称
    desired_caps['platformName'] = 'Android'
    # 平台测版本
    desired_caps['platformVersion'] = '6.0'
    # 设备名称： 在 appium sdk 中获取得到   【命令：adb devices】
    desired_caps['deviceName'] = 'emulator-5554'
    # com.android.settings/com.android.settings.Settings
    # 测试包的名称
    desired_caps['appPackage'] = 'com.android.settings'
    # app-demo 每个页面都是一个appActivity， 默认指定的页面
    # 获取命令： adb logcat | grep -i displayed
    desired_caps['appActivity'] = 'com.android.settings.Settings'

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    print("启动【设置】应用")
    driver.quit()
