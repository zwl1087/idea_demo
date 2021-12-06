#!/usr/bin/python3
'''
author = zhaowenlong
project = pytestProject
date = 2021/11/21

'''
from selenium.webdriver.common.by import By

from test_pytest.page_object.base_apge import BasePage
from test_pytest.page_object.contact_page import ContactPage
from test_pytest.page_object.add_menber_page import AddMemberPage


class MainPage(BasePage):

    # 子类如果和父类的类属性重名，那么子类在实例化过程中会覆盖父类的类属性
    # 调用过程： MainPage() 实例化时候，将 _base_url 重写至 父类(BasePage)的_base_url属性
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_conctact(self):
        self.add_log("info", "从主页跳转至通讯录页面 ")
        _contact_page = (By.ID, "menu_contacts")
        self.find(_contact_page).click()
        return ContactPage(self.driver)  # 返回要跳转至的页面的PO;解决多个页面有交互的问题

    def goto_add_member(self):
        print(" 跳转至添加成员 ")
        _goto_add_member = (By.CSS_SELECTOR, ".ww_indexImg_AddMember")
        self.find(_goto_add_member).click()
        return AddMemberPage(self.driver)
