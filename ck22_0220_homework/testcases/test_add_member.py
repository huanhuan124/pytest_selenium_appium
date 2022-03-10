import time

import yaml
from selenium import webdriver

# from page_object.main_page import Main_Page
from ck22_0220_homework.page_object.main_page import Main_Page


class TestAddMember:


    def setup_class(self):
        self.main_p = Main_Page()
        self.main_p.login()

    def teardown_class(self):
        # self.main_p.driver.quit()
        pass

    def teardown(self):
        self.main_p.back_start_page()

    def test_add_member(self):

        username = '金克斯7'
        acctid = 'jinkesi7'
        phone = '13011002200'
        mem_list = self.main_p.goto_add_member_page().add_member(username, acctid, phone).get_member_list()
        assert '金克斯5' in mem_list


    def test_add_member_fail(self):
        username = '金克斯7'
        acctid = 'jinkesi7'
        phone = '1301100220'
        res = self.main_p.goto_add_member_page().add_member_fail(username, acctid, phone)
        assert "请填写正确的手机号码" in res


