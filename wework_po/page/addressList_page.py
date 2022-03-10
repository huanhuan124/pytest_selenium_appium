import logging

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from wework_po.base.wework_app import Wework_app



class AddressList_page(Wework_app):

    def goto_addMember(self):

        logging.info("点击添加成员")
        self.swipe_find(3,'添加成员').click()
        from wework_po.page.addMember_page import AddMember_page
        logging.info("跳转到添加成员页")
        return AddMember_page(self.driver)

    def goto_search(self):
        logging.info("点击放大镜")
        # 通过查找公司那一个级别的后面的兄弟节点。following-sibling 就是找到当前结点 后面的所有结点,如果找到多个元素，下标从1开始，比如 1,2,3...
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@text='环易网络科技有限公司']/../../../following-sibling::*/*[1]").click()
        logging.info("跳转到搜索页")
        from wework_po.page.search_page import Search_page
        return Search_page(self.driver)