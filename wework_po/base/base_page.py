import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class Base_page:

    def __init__(self,driver: WebDriver = None):
        self.driver = driver
        # print("Base_page 初始化这时候的driver是：-------")
        # print(self.driver)

    def find(self, by,locator):
        # self.driver.find_element_by_xpath(f'//*[@text={text}]')
        return self.driver.find_element(by,locator)

    def find_click(self, by,locator):
        self.find(by,locator).click()

    def finds(self,by,locator):
        return self.driver.find_elements(by, locator)

    def find_sendkeys(self,by,locator,text):
        self.find(by,locator).send_keys(text)

    def back(self, num):
        for i in range(num):
            self.driver.back()

    def swipe_find(self, num, text ):
        #向上滑动，x坐标不变，y变

        for i in range(num):
            try:
                element = self.driver.find_element_by_xpath(f"//*[@text='{text}']")
                return element
            except:
                print('未找到')
                #获取屏幕的宽高
                width = self.driver.get_window_size()['width']
                height = self.driver.get_window_size()['height']
                start_x = width/2
                start_y = height*0.8
                end_x = start_x
                end_y = height*0.3
                #start_x，start_y 开始坐标，end_x, end_y 结束坐标，duration 滑动持续时间，默认5ms
                self.driver.swipe(start_x,start_y,end_x,end_y,duration=2000)
            if i == num -1:
                raise NoSuchElementException(f'找了{num}次，没找到')

    def get_data(self):
        # C:\Users\zenghuan\PycharmProjects\test_selenium_appium\wework_po\datas\datas

        with open("C:/Users/zenghuan/PycharmProjects/test_selenium_appium/wework_po/datas/datas.yml", 'r',
                  encoding='utf-8') as f:
            result = yaml.safe_load(f)
        # print(result)
        # print(result.get("datas"))
        return result.get("datas"),result.get("ids"),result.get('searchkey')
