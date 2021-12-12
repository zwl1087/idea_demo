#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2021/12/12

"""
from appium.webdriver.common.mobileby import MobileBy

from base_page import BasePage
from page.address_list_page import AddressListPage


class MainsPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def goto_address_list_page(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()

        return AddressListPage(self.driver)
