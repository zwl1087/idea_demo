#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2021/12/5

"""
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from test_appium_exeise.main_page import MainPage


class TestWorkWeixin():

    def setup_class(self):
        # self.mains = MainPage()
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
            "dontStopAppOnReset": True,
            # 等待页面处于idle状态 ，默认10s
            "settings[waitForIdleTimeout]": 0,
            # "chromedriverExecutable": "D:\webdirver\chromedriver66\chromedriver.exe",
            "unicodeKeyboard": True,
            "resetKeyboard": True,
            # 防止 清缓存数据 Don't reset app state before this session. See here for more details
            "noReset": True
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(10)



    def teardown_class(self):
        self.driver.back()

    @pytest.mark.skip
    def test_add_member(self):
        # 添加成员
        res = self.mains.goto_contact().goto_add_member().add_member()
        # 获取结果
        # 断言
        assert "添加成功" == res

    def swipe_find(self, name, num = 3):
        """
        根据查询内容, 和查询次数来循环查找
        :param num:  查询次数, 默认查询3次
        :param name:  查询的内容
        :return: 如果查询到了， 返回该元素, 查询不到就返回 NoSuchElementException 异常
        """
        for i in range(num):
            try:
                ele = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{name}']")
                print(" 元素找到了", f"//*[@text='{name}']")
                return ele
            except:
                print("元素没有找到", f"//*[@text='{name}']")
                size = self.driver.get_window_size()
                width = size["width"]
                height = size["height"]

                start_x = end_x = width / 2
                start_y = height * 0.8
                end_y = height * 0.2

                self.driver.swipe(start_x, start_y, end_x, end_y, duration = 2000)
                print(f"第{ i + 1 }次滑动屏幕")

            if i == num - 1:
                raise NoSuchElementException(f"总共查询了{num}次, 没有查询到")


    def test_punch_clock(self):


        # 进入【工作台】页面
        self.driver.find_element(MobileBy.XPATH, '//*[@text="工作台"]').click()
        # 滚动查找元素【打卡】并点击
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                                'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("打卡").instance(0));').\
        #     click()

        ele = self.swipe_find("打卡")
        ele.click()

        # 点击【外出打卡】
        self.driver.find_element(MobileBy.XPATH, '//*[@text="外出打卡"]').click()
        # 点击【第**次外出】
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"次外出")]').click()
        # 检查【外出打卡成功】
        assert len(self.driver.find_elements(By.XPATH, '//*[@text="外出打卡成功"]')) >= 1









