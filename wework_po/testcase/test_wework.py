import logging

import pytest
from appium.webdriver.common.mobileby import MobileBy

from wework_po.base.base_page import Base_page
from wework_po.base.wework_app import Wework_app
from wework_po.page.main_page import Main_page

"""
同时配置了conftest.py和pytes.ini，只会生效conftest里面的内容
conftest里面的manage_logs加了fixture，并且是自动引用的，在测试用例中不需要引用，无感执行，会直接生成带日期时间的日志文件

用PO模式实现了企业微信app：
1、添加企业微信用户
2、删除企业微信用户
3、增加了日志
4、实现了数据驱动

"""


class Test_wework():
    #要先实例化，才能调用get_data，不能直接Base_page.get_data()

    addMember_data, ids, searchkey = Base_page().get_data()

    def setup_class(self):
        logging.info("开始企业微信测试")
        self.app = Wework_app()


    def setup(self):

        self.main = self.app.start().goto_main()


    def teardown(self):
        logging.info("完成本次测试")
        self.main.back(2)

    def teardown_class(self):
        logging.info("结束测试")
        self.app.stop()


    @pytest.mark.parametrize('name,phone', addMember_data, ids=ids)
    def test_addMember(self,name,phone):
        logging.info(f"输入数据：{name, phone}")
        result = self.main.goto_addresslist().goto_addMember().goto_editMember().edit(name,phone)
        assert '添加成功' == result

    @pytest.mark.parametrize('searchkey',searchkey)
    def test_deleteMember(self,searchkey):

        start_elements_len,end_elements_len = self.main.goto_addresslist().goto_search().goto_userinfo(searchkey).goto_userInfo_edit().goto_editMember().edit_delete()

        assert start_elements_len - 1 == end_elements_len

