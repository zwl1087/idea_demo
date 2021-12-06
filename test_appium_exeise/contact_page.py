#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2021/12/5

"""
from selenium.webdriver.common.by import By

from test_appium_exeise.add_member_page import AddMemberPage
from test_appium_exeise.base_page import BasePage


class ContactPage(BasePage):

    def goto_add_member(self):

        self.driver.find_element(By.XPATH, '//*[@text="添加成员"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="手动输入添加"]').click()

        return AddMemberPage()


