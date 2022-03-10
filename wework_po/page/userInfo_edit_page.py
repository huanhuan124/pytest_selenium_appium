import logging

from appium.webdriver.common.mobileby import MobileBy

from wework_po.base.wework_app import Wework_app


class UserInfo_edit_page(Wework_app):

    def goto_editMember(self):
        edit_element = (MobileBy.XPATH, '//*[@text="编辑成员"]')
        logging.info("点击编辑成员")
        # self.driver.find_element_by_xpath('//*[@text="编辑成员"]').click()
        self.find_click(*edit_element)
        logging.info("跳转到编辑成员页")
        from wework_po.page.editMember_page import EditMember_page
        return EditMember_page(self.driver)