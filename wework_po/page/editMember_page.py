import logging


from appium.webdriver.common.mobileby import MobileBy

from wework_po.base.wework_app import Wework_app



class EditMember_page(Wework_app):


    def edit(self, name, phone ):

        user_element = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/bsm']",name)
        password_element = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/hgi']",phone)
        save_element = (MobileBy.XPATH, '//*[@text="保存"]')
        toast_element = (MobileBy.XPATH, "//*[@class='android.widget.Toast']")

        logging.info("输入用户名")
        # self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/bsm']").send_keys(name)
        self.find_sendkeys(*user_element)
        logging.info("输入手机号")
        # self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/hgi']").send_keys(phone)
        self.find_sendkeys(*password_element)
        logging.info("点击保存")
        # self.driver.find_element_by_xpath('//*[@text="保存"]').click()
        self.find_click(*save_element)
        logging.info("保存成功，弹层toast")
        # element_toast = self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']")
        # result = element_toast.get_attribute('text')
        result = self.find(*toast_element).get_attribute('text')
        return result

    def edit_delete(self):
        confirm_element = (MobileBy.XPATH, '//*[@text="确定"]')
        num_element =  (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/esq']")
        logging.info("点击删除")
        self.swipe_find(3, '删除成员').click()
        logging.info("点击确定")
        # self.driver.find_element_by_xpath('//*[@text="确定"]').click()
        self.find_click(*confirm_element)
        logging.info("跳转到搜索结果页，获取删除后的联系人个数")
        from wework_po.page.search_page import Search_page
        # return Search_page(self.driver)
        return Search_page(self.driver).get_memberNum(num_element)