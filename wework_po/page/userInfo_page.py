import logging

from appium.webdriver.common.mobileby import MobileBy

from wework_po.base.wework_app import Wework_app


class UserInfo_page(Wework_app):

    def goto_userInfo_edit(self):
        shengluehao_element = (MobileBy.XPATH, "//*[@text='个人信息']/../../../../following-sibling::*[1]")
        logging.info("点击右上角的三个点")
        # 通过找到个人信息的兄弟节点
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='个人信息']/../../../../following-sibling::*[1]").click()
        self.find_click(*shengluehao_element)
        logging.info("跳转到个人信息编辑页")
        from wework_po.page.userInfo_edit_page import UserInfo_edit_page
        return UserInfo_edit_page(self.driver)
