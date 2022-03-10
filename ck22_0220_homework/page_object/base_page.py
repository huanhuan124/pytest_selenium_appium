from selenium import webdriver


class Base_Page:
    """
    问题：Driver 初始化如果绑定在某个页面类中，那么多个页面类都需要进行初始化操作
    解决方案：Driver 初始化的部分放在 BasePage 中，其他 Page 类继承 BasePage。子类可以使用父类的属性，直接通过 self.driver 调用 driver 实例对象

    """
    def __init__(self,base_driver=None):
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(3)
        else:
            self.driver = base_driver

    def find(self, by, locator = None):
        if locator is None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by,locator)
