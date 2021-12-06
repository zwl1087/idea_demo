#!/usr/bin/python3
'''
author = zhaowenlong
project = pytestProject
date = 2021/11/21

'''
from selenium.webdriver.common.by import By
from test_pytest.page_object.base_apge import BasePage

class ContactPage(BasePage):

    _base_url = "https://work.weixin.qq.com/wework_admin/frame#contacts"

    def get_member_list(self):

        _name_list = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")

        eles = self.finds(_name_list)
        men_name_list = [ele.text for ele in eles]

        print("检查通讯录中添加成功了")
        return men_name_list

    # 循环导入引起报错解决，在方法内导入
