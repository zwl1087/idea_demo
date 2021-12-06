#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2021/11/21
"""
from selenium.webdriver.common.by import By

from test_pytest.page_object.base_apge import BasePage
from test_pytest.page_object.contact_page import ContactPage


class AddMemberPage(BasePage):
    # 添加成员信息
    _username = (By.ID, 'username')
    _user_acct_id = (By.ID, 'memberAdd_acctid')
    _user_phone = (By.CSS_SELECTOR, '.ww_telInput_mainNumber')

    def goto_contact(self) -> object:
        print(" 跳转至通讯录 ")
        return ContactPage(self.driver)

    def add_member(self, men_name, mem_acct_id, mem_phone):
        print(" 成员添加完成，跳转至通讯录 ")

        self.find(self._username).send_keys(men_name)
        self.find(self._user_acct_id).send_keys(mem_acct_id)
        self.find(self._user_phone).send_keys(mem_phone)
        # 保存
        _save_user_info = (By.CSS_SELECTOR, ".js_btn_save")
        self.find(_save_user_info).click()

        return ContactPage(self.driver)

    def add_member_fail_by_name(self):
        """ name不填写，一个添加成员的反例操作。
        :return:
        """
        self.find(self._user_acct_id).send_keys("10000")
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("13188881111")
        # 点击保存
        # self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        error_list = self.driver.find_elements(By.CSS_SELECTOR, ".ww_inputWithTips_tips")
        # 寻找所有的错误信息，如果不为空，则返回
        error_message = [ele.text for ele in error_list if ele.text != ""]
        return error_message

