import logging

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from wework_po.base.base_page import Base_page



class Wework_app(Base_page):


    def start(self):
        logging.info("开始本次测试")
        if self.driver == None:

            # print("Wework_app没有driver//////////////")
            # print(self.driver)
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            # device名称  三星 4c545459594d573398  10.0
            desired_caps['deviceName'] = '4c545459594d573398'
            # huawei  3HX7N16C24009682  8.0
            # desired_caps['deviceName'] = '3HX7N16C24009682'
            # 手机实际的版本
            desired_caps['platformVersion'] = '10.0'
            # apk包名
            desired_caps['appPackage'] = 'com.tencent.wework'
            # activity名
            desired_caps['appActivity'] = '.launch.LaunchSplashActivity'

            desired_caps['unicodeKeyBoard'] = 'true'
            desired_caps['resetKeyBoard'] = 'true'
            # 比如首次打开的时候会有弹窗提示，如果设置了以后，第一次弹窗点击确定后，第二次运行的时候，不会有弹窗
            desired_caps['noReset'] = 'true'
            # desired_caps['fullReset']= 'true'
            # 不用每次都重新启动
            desired_caps['dontStopAppOnReset'] = 'true'

            # 跳过 uiautomator2 server的安装
            desired_caps['skipServerInstallation'] = 'true'
            # 跳过设备初始化
            desired_caps['skipDeviceInitialization'] = 'true'
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
            self.driver.implicitly_wait(10)
            # print('start  driver 初始化完成时')
            # print(self.driver)
        else:
            # print("Wework_app有driver*********")
            # print(self.driver)
            #启动APP
            self.driver.launch_app()

        #返回的是类的实例
        return self

    def goto_main(self):
        logging.info("跳转到首页")
        from wework_po.page.main_page import Main_page
        # print('wowork_app goto_main  driver')
        # print(self.driver)
        return Main_page(self.driver)

    def stop(self):

        self.driver.quit()

    def wait_for_text(self,text):
        try:
            WebDriverWait(self.driver,5).until(lambda x : x.find_element(MobileBy.XPATH,f"//*[@text='{text}']"))
            return True
        except:
            return False





