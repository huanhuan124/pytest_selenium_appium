from selenium.webdriver.common.by import By

# from page_object.base_page import Base_Page
# from page_object.work_page import Work_Page
from ck22_0220_homework.page_object.work_page import Work_Page


class Contact_Page(Work_Page):
    _BASE_URL = "https://work.weixin.qq.com/wework_admin/frame#index"

    def get_member_list(self):
        """
        获取成员列表
        :return:
        """
        ele_list = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_tr td:nth-child(2)")
        # 把元素列表 转换为名称列表，使用列表推导式（python-列表）
        member_list = [ele.text for ele in ele_list]
        # 成员的名称的列表
        return member_list