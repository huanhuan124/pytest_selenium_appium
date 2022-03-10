import logging

from appium.webdriver.common.mobileby import MobileBy

from wework_po.base.wework_app import Wework_app



class AddMember_page(Wework_app):

    def goto_editMember(self):
        element = (MobileBy.XPATH, '//*[@text="手动输入添加"]')
        logging.info("点击手动输入添加")
        # self.driver.find_element_by_xpath('//*[@text="手动输入添加"]').click()
        self.find_click(*element)

        from wework_po.page.editMember_page import EditMember_page
        logging.info("跳转到编辑成员页")
        return EditMember_page(self.driver)
