from selenium import webdriver
from selenium.webdriver.common.by import By
#
# from page_object.add_member_page import Add_Member_Page
# from page_object.base_page import Base_Page
# from page_object.contact_page import Contact_Page
# from page_object.work_page import Work_Page
from ck22_0220_homework.page_object.add_member_page import Add_Member_Page
from ck22_0220_homework.page_object.contact_page import Contact_Page
from ck22_0220_homework.page_object.work_page import Work_Page


class Main_Page(Work_Page):

    _BASE_URL = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_add_member_page(self):
        # self.driver = webdriver.Chrome()
        # self.driver.find_element(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()
        self.find(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()

        return Add_Member_Page(self.driver)


    def goto_contact_page(self):
        return Contact_Page()

