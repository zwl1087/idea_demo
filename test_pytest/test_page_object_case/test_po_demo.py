#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2021/11/21
"""
import pytest

from test_pytest.page_object.main_page import MainPage


class TestPoDemo:
    def setup_class(self):
        # 实例化 MainPage()
        self.main = MainPage()

    def teardown_class(self):
        # 关闭浏览器
        self.main.driver.quit()

    # 从首页进入添加成员页面，在添加成员页面填写人员信息，最后在通讯录里检查是否添加成功
    @pytest.mark.skip
    @pytest.mark.parametrize("mem_name, men_acct_id, mem_phone", [("hotzz6", "202111210006", "18530061121")])
    def test_add_member(self, mem_name, men_acct_id, mem_phone):
        # 采用链式调用，可以有效的避免多次实例化的操作
        res = self.main.goto_add_member().add_member(mem_name, men_acct_id, mem_phone).get_member_list()
        print(" 测试执行完成了 ")
        assert mem_name in res

    def test_add_member_fail(self):
        # 错误信息列表
        error_list = self.main.goto_add_member(). \
            add_member_fail_by_name()
        assert "请填写姓名" in error_list
