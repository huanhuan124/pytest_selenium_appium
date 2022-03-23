from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.by import By


class TestMajorSelenium:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):

        self.driver.quit()

    @pytest.mark.skip
    def test_click(self):
        self.driver.get('http://sahitest.com/demo/clicks.htm')
        #单击
        ele_click = self.driver.find_element(By.XPATH,'//input[@value="click me"]')
        #右击
        ele_right_click = self.driver.find_element(By.XPATH,'//*[@value="right click me"]')
        #双击
        ele_double_click = self.driver.find_element(By.XPATH,'//*[@value="dbl click me"]')
        action = ActionChains(self.driver)
        action.click(ele_click)
        action.context_click(ele_right_click)
        action.double_click(ele_double_click)
        sleep(3)
        action.perform()
        sleep(3)


    @pytest.mark.skip
    def test_moveto(self):
        self.driver.get("http://www.baidu.com")
        ele_move = self.driver.find_element(By.XPATH,'//*[@id="s-usersetting-top"]')
        action = ActionChains(self.driver)
        action.move_to_element(ele_move)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_drgtodrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        ele_drag = self.driver.find_element(By.ID,'dragger')
        ele_drop = self.driver.find_element(By.XPATH,"/html/body/div[2]")
        action = ActionChains(self.driver)
        action.drag_and_drop(ele_drag,ele_drop)
        action.perform()
        sleep(3)




if __name__ == '__main__':
    pytest.main(['-v','-s','test_major_selenium.py'])