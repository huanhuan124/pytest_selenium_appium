from time import sleep
from appium import webdriver

class TestXueqiu:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        #device名称
        desired_caps['deviceName'] = '4c545459594d573398'
        #手机实际的版本
        desired_caps['platformVersion'] = '10.0'
        # apk包名
        desired_caps['appPackage'] = 'com.xueqiu.android'
        # activity名
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        # 比如首次打开的时候会有弹窗提示，如果设置了以后，第一次弹窗点击确定后，第二次运行的时候，不会有弹窗
        desired_caps['noReset'] = 'true'
        # desired_caps['fullReset']= 'true'
        # 不用每次都重新启动
        desired_caps['dontStopAppOnReset'] = 'true'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass
        # self.driver.quit()

    def test_search(self):
        self.driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
        sleep(2)
