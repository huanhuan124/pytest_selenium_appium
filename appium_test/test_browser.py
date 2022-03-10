from time import sleep

from appium import webdriver


class TestBrowser:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # device名称  三星  4c545459594d573398  10.0
        desired_caps['deviceName'] = '4c545459594d573398'
        # huawei  3HX7N16C24009682  8.0
        # desired_caps['deviceName'] = '3HX7N16C24009682'
        # 手机实际的版本
        desired_caps['platformVersion'] = '10.0'

        # 自带的浏览器用browser
        # desired_caps['browserName'] = 'Browser'

        # chrome浏览器用
        desired_caps['browserName'] = 'chrome'

        desired_caps['chromeOptions'] = {'w3c': False}
        #chromedriverExecutable
        #chrome 对应的driver
        # desired_caps['chromedriverExecutable'] = 'D:/phoneChromedriver/chrome/chromedriver.exe'

        # 三星手机自带浏览器 对应的driver
        # desired_caps['chromedriverExecutable'] = 'D:/phoneChromedriver/samsung/chromedriver'

        # huawei手机自带浏览器 对应的driver
        # desired_caps['chromedriverExecutable'] = 'D:/phoneChromedriver/huawei/chromedriver.exe'

        # sanxing 华为  手机chrome浏览器 对应的driver  版本=98.0.4758.101
        desired_caps['chromedriverExecutable'] = 'D:/phoneChromedriver/chrome/chromedriver.exe'

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass
        # self.driver.quit()

    def test_search(self):
        self.driver.get("http://m.taobao.com")
        sleep(3)