#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2021/12/12

"""
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from base_page import BasePage


class AddMemberPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def add_member(self):
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"姓名")]/../android.widget.EditText').send_keys(
            "daadddaa2")
        self.driver.find_element(MobileBy.XPATH,
                                 '//*[contains(@text,"手机")]//following-sibling::*//android.widget.EditText').send_keys(
            "18122345678")
        self.driver.find_element(MobileBy.XPATH, '//*[@text="保存"]').click()

        sleep(3)

        result_toast = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").get_attribute(
            "text")
        return result_toast
