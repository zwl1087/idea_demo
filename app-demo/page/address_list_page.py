#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2021/12/12

"""
from appium.webdriver.common.mobileby import MobileBy

from base_page import BasePage
from page.add_member_page import AddMemberPage


class AddressListPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def goto_add_member_page(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()

        return AddMemberPage(self.driver)
