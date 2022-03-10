import logging

import pytest
from appium.webdriver.common.mobileby import MobileBy

from wework_po.base.wework_app import Wework_app


class Search_page(Wework_app):

    memberlist = []



    def goto_userinfo(self,searchkey):
        search_element = (MobileBy.XPATH, '//*[@text="搜索"]',searchkey)
        memberlist_element = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/esq']")
        logging.info("输入搜索词")
        # 输入搜索词
        # self.driver.find_element_by_xpath('//*[@text="搜索"]').send_keys(searchkey)
        self.find_sendkeys(*search_element)

        exists = self.wait_for_text('联系人')
        # 如果没有搜索结果
        if not exists:
            logging.info("没有搜索结果")
            pytest.xfail(reason=f"无搜索结果：{searchkey}")

        # 如果有搜索结果，获取联系人下方的个数
        logging.info("有搜索结果")
        start_elements_len = self.get_memberNum(memberlist_element)

        logging.info("点击第一个联系人")
        # 点击第一个联系人

        self.driver.find_elements_by_xpath("//*[@resource-id='com.tencent.wework:id/esq']")[0].click()
        logging.info("跳转到个人信息页")
        from wework_po.page.userInfo_page import UserInfo_page
        return UserInfo_page(self.driver)



    def get_memberNum(self,text):
        elements_size = self.finds(*text)
        elements_len = len(elements_size)
        self.memberlist.append(elements_len)
        print('联系人列表：')
        print(self.memberlist)
        return self.memberlist
