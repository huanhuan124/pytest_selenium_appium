from selenium import webdriver

from selenium_test.base import Base


class TestWindows(Base):
    # def setup(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.implicitly_wait(2)
    #     self.driver.maximize_window()
    #
    # def teardown(self):
    #     self.driver.quit()

    def test_windows(self):
        self.driver.get("http://www.baidu.com")
        #点击登录
        self.driver.find_element_by_id("s-top-loginbtn").click()
        #打印当前窗口
        print(self.driver.current_window_handle)
        # 打印所有窗口
        print(self.driver.window_handles)
        # 点击立即注册
        self.driver.find_element_by_id("TANGRAM__PSP_11__regLink").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        #切换到立即注册的窗口
        self.driver.switch_to.window(self.driver.window_handles[-1])
        #输入注册的用户名，密码
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("testname")
        self.driver.find_element_by_id('TANGRAM__PSP_4__phone').send_keys("13201010203")
        # 切换到上一个窗口
        self.driver.switch_to.window(self.driver.window_handles[0])
        # 输入用户名，密码
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("zenghuan")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("123456")
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
