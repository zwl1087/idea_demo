#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2021/12/12

"""
from appium import webdriver

from page.main_page import MainsPage

"""
存放app相关的操作
"""


class App:

    def start(self):
        desire_cap = {
            "platformName": "Android",
            "platformVersion": "6.0",
            "deviceName": "emulator-5554",
            # 重要的：通过命令获取package/activity :
            # adb logcat ActivityManager:I | grep "cmp"
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            # 跳过设备初始化 ,跳过settings.apk的安装与设置
            "skipDeviceInitialization": True,
            # 跳过 uiautomator2 服务安装
            "skipServerInstallation": True,
            # 在运行测试之前，不停止 app-demo ，或者说不重新启动app，必须注意： 执行测试用例时都在同一个相对页面上
            "dontStopAppOnReset": True,
            # 等待页面处于idle状态 ，默认10s
            "settings[waitForIdleTimeout]": 0,
            # "chromedriverExecutable": "D:\webdirver\chromedriver66\chromedriver.exe",
            "unicodeKeyboard": True,
            "resetKeyboard": True,
            # 防止 清缓存数据 Don't reset app-demo state before this session. See here for more details
            "noReset": True
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(10)

        # return self

    def stop(self):
        self.driver.quit()

    def restart(self):
        self.driver.launch_app()
        # self.driver.start_activity("","")

    def goto_main_page(self):
        return MainsPage(self.driver)
