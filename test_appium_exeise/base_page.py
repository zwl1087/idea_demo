#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2021/12/5

"""
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import faker


class BasePage():

    def setup_class(self):
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
            # 在运行测试之前，不停止 app ，或者说不重新启动app，必须注意： 执行测试用例时都在同一个相对页面上
            # "dontStopAppOnReset": True,

            # 等待页面处于idle状态 ，默认10s
            "settings[waitForIdleTimeout]": 0,

            "chromedriverExecutable": "D:\webdirver\chromedriver66\chromedriver.exe",
            "unicodeKeyboard": True,
            "resetKeyboard": True,
            # 防止 清缓存数据 Don't reset app state before this session. See here for more details
            "noReset": True
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):
        # 返回上一页
        # self.driver.back()
        self.driver.quit()

    # 基类中封装一个获取姓名的方法
    @staticmethod
    def get_name_cn():
        fa = faker.Faker("zh_CN")
        return fa.name()

    # 基类中封装一个获取电话号码的方法
    @staticmethod
    def get_phone_num_cn():
        fa = faker.Faker("zh_CN")
        return fa.phone_number()

    def swipe_find(self, name, num = 3):
        """
        根据查询内容, 和查询次数来循环查找
        :param num:  查询次数, 默认查询3次
        :param name:  查询的内容
        :return: 如果查询到了， 返回该元素, 查询不到就返回 NoSuchElementException 异常
        """
        for i in range(num):
            try:
                ele = self.driver.find_element(MobileBy.XPATH, f"//*[@text={name}]")
                return ele
            except:
                size = self.driver.get_window_size()
                width = size["width"]
                height = size["height"]

                start_x = end_x = width / 2
                start_y = height * 0.8
                end_y = height * 0.2

                self.driver.swipe(start_x, start_y, end_x, end_y, duration = 2000)
            if i == num - 1:
                raise NoSuchElementException(f"总共查询了{i}次, 没有查询到")


if __name__ == '__main__':
    print(BasePage.get_name_cn())
    print(BasePage.get_phone_num_cn())
