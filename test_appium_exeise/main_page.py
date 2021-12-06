#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2021/12/5

"""
from selenium.webdriver.common.by import By

from test_appium_exeise.base_page import BasePage
from test_appium_exeise.contact_page import ContactPage



class MainPage(BasePage):

    def goto_contact(self):

        self.driver.find_element(By.XPATH, '//*[@text="通讯录"]').click()

        return ContactPage()
