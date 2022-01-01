#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2021/12/12

"""
from base.app import App


class TestAddMember():

    def setup_class(self):
        self.main = App()
        self.main.start()

    def teardown_class(self):
        self.main.stop()

    def test_add_member(self):
        res = self.main.goto_main_page().goto_address_list_page().goto_add_member_page().add_member()

        assert "添加成功" in res
