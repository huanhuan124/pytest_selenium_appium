from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.by import By







class TestTouchActions:

    def setup(self):
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('w3c',False)
        self.driver = webdriver.Chrome(options=opt)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()


    def test_scroll(self):
        self.driver.get("http://www.baidu.com")
        sleep(2)
        ele = self.driver.find_element(By.ID,'kw')
        ele.send_keys("selenium 测试")
        ele_search = self.driver.find_element(By.ID,'su')
        touchaction = TouchActions(self.driver)
        touchaction.tap(ele_search)
        touchaction.scroll_from_element(ele_search,0,10000)
        touchaction.perform()
        sleep(3)


if __name__ == '__main__':
    pytest.main(['-v','-s','test_TouchActions.py'])