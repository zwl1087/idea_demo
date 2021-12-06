#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2021/12/5

"""
from selenium.webdriver.common.by import By

from test_appium_exeise.base_page import BasePage


class AddMemberPage(BasePage):

    def add_member(self):

        self.driver.find_element(By.XPATH, "").send_keys("daadddaa")
        self.driver.find_element(By.XPATH, "").send_keys("18112345678")
        self.driver.find_element(By.XPATH, "").click()

        result_toast = self.driver.find_element(By.XPATH, "//*[@class='']").get_attribute("text")

        return result_toast
