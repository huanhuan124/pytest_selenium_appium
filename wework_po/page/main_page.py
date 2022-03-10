import logging

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from wework_po.base.wework_app import Wework_app



class Main_page(Wework_app):
    addresslist_element = (MobileBy.XPATH, '//*[@text="通讯录"]')

    def goto_addresslist(self):
        # self.driver.find_element_by_xpath('//*[@text="通讯录"]').click()
        logging.info("点击通讯录")
        #点击通讯录
        self.find_click(*self.addresslist_element)

        # self.find(MobileBy.XPATH,'//*[@text="通讯录"]')
        from wework_po.page.addressList_page import AddressList_page
        # print('Main_page  driver')
        # print(self.driver)
        logging.info("跳转到通讯录列表页")
        return AddressList_page(self.driver)