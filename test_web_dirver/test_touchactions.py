#!/usr/bin/python3
'''
author = zhaowenlong
project = pytestProject
date = 2021/11/20

'''
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestTouchActions():
    def setup_class(self):
        option = Options()
        option.add_experimental_option("w3c",False)
        # option.debugger_address = "localhost:9222"
        self.driver = webdriver.Chrome(options=option)
    #
    #
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
    # def teardown_class(self):
    #     self.driver.close()
    @pytest.mark.skip
    def test_touchactions_scroll(self):
        self.driver.get("https://baidu.com")
        sleep(3)
        els_input = self.driver.find_element(By.ID,"kw")
        els_seach = self.driver.find_element(By.ID,"su")
        print(els_input)
        # self.driver.find_element(By.ID,"kw").send_keys("selenium高级测试")
        els_input.send_keys("selenium高级测试")
        action = TouchActions(self.driver)
        action.tap(els_seach)
        action.perform()

        action.scroll_from_element(els_input,0,10000).perform()
        sleep(5)
    def test_assert_list(self):
        a = [1,2,3,4]
        a_1 = [1,2,3,4,[1,2]]
        b = [1,2,3,4]
        b_1 = [1, 2, 3, 4, [1, 2]]
        b_2 = [1, 2, 3, 4, [1, 2],(1,2)]
        b_3 = [1, 2, 3, 4, [1, 2],(1,2)]
        c = (1,2)
        assert c in b_3
        # assert a == b and a_1 == b_1 and b_2 == b_3











