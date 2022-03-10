import time

import yaml

# from page_object.base_page import Base_Page
from ck22_0220_homework.page_object.base_page import Base_Page


class Work_Page(Base_Page):

    _BASE_URL = ""

    def login(self):
        # 1. 访问企业微信主页面
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        print(f'当前传过来的base_url是：{self._BASE_URL}')
        self.driver.get(self._BASE_URL)
        # 2. 定义cookie，cookie信息从已经写入的cookie文件中获取
        cookie = yaml.safe_load(open("../data/cookie.yaml"))
        # 3. 植入cookie
        for c in cookie:
            self.driver.add_cookie(c)
        time.sleep(3)
        # 4.再次访问企业微信页面，发现无需扫码自动登录，而且可以多次使用
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.get(self._BASE_URL)

    def back_start_page(self):
        self.driver.get(self._BASE_URL)