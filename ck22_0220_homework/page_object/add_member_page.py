from selenium.webdriver.common.by import By

# from page_object.base_page import Base_Page
# from page_object.contact_page import Contact_Page
# from page_object.work_page import Work_Page
from ck22_0220_homework.page_object.contact_page import Contact_Page
from ck22_0220_homework.page_object.work_page import Work_Page


class Add_Member_Page(Work_Page):
    # 页面元素不要暴露出去，只给页面的方法提供使用。
    _INPUT_USERNAME = (By.ID, "username")

    def add_member(self, username, acctid, phone):
        """
        添加成员功能
        添加完成后返回到通讯录页面
        """
        # 问题： driver实例化了多次，影响用例的执行
        # 解决方案： 让driver 只实例化一次
        # self.find(By.ID, "username").send_keys("金克斯6")
        self.find(self._INPUT_USERNAME).send_keys(username)
        self.find(By.ID, "memberAdd_acctid").send_keys(acctid)
        self.find(By.ID, "memberAdd_phone").send_keys(phone)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()

        return Contact_Page(self.driver)

    def add_member_fail(self, username, acctid, phone):
        self.find(self._INPUT_USERNAME).send_keys(username)
        self.find(By.ID, "memberAdd_acctid").send_keys(acctid)
        self.find(By.ID, "memberAdd_phone").send_keys(phone)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        eles = self.driver.find_elements(By.CSS_SELECTOR, ".ww_inputWithTips_tips")
        error_list = [ele.text for ele in eles]
        return error_list
