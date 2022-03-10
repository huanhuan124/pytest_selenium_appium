from time import sleep

from selenium.webdriver import ActionChains

from selenium_test.base import Base


class TestFrame(Base):

    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        #切到frame里面
        self.driver.switch_to.frame('iframeResult')
        drag = self.driver.find_element_by_id('draggable')
        drop = self.driver.find_element_by_id('droppable')
        #拖拽
        action = ActionChains(self.driver)
        action.drag_and_drop(drag,drop).perform()
        #点击alert框的确定
        self.driver.switch_to.alert.accept()
        #切换回上一个frame
        self.driver.switch_to.parent_frame()
        #点击运行
        self.driver.find_element_by_id('submitBTN').click()

    def test_upload(self):
        self.driver.get("https://image.baidu.com/")
        # sleep(5)
        # self.driver.find_element_by_class_name('st_camera_on').click()
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        self.driver.find_element_by_id('stfile').send_keys('C:/Users/zenghuan/PycharmProjects/test_selenium_appium/selenium_test/JMETERCAR81434879_ZSBD202109170000001.png')
        sleep(2)