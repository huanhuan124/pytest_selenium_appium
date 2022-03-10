from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWework:

    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # device名称  三星 4c545459594d573398  10.0
        desired_caps['deviceName'] = '4c545459594d573398'
        #huawei  3HX7N16C24009682  8.0
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

    def teardown(self):
        pass
        #self.driver.quit()

    def test_addMember(self):
       """
        通讯录添加成员用例步骤

            打开【企业微信】应用
            进入【通讯录】页面
            点击【添加成员】
            点击【手动输入添加】
            输入【姓名】【手机号】并点击【保存】

        验证点：登录成功提示信息
       :return:
       """

       self.driver.find_element_by_xpath('//*[@text="通讯录"]').click()
       #self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0)').click()

       #self.driver.find_element_by_xpath('//*[@text="添加成员"]').click()
       search_script = 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0));'
       self.driver.find_element_by_android_uiautomator(search_script).click()

       self.driver.find_element_by_xpath('//*[@text="手动输入添加"]').click()
       self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/bsm']").send_keys('金克斯3')
       self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/hgi']").send_keys('13012312010')
       self.driver.find_element_by_xpath('//*[@text="保存"]').click()
       element_toast = self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']")
       result = element_toast.get_attribute('text')
       assert '添加成功' == result

       sleep(2)


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



    def test_workdaka(self):
        """
        前提条件：
            1、提前注册企业微信管理员帐号
            2、手机端安装企业微信
            3、企业微信 app 处于登录状态
        实现打卡功能
            打开【企业微信】应用
            进入【工作台】页面
            点击【打卡】
            选择【外出打卡】tab
            点击【第 N 次打卡】
            验证点：提示【外出打卡成功】
        """

        self.driver.find_element_by_xpath('//*[@text="工作台"]').click()
        self.swipe_find(3,'打卡').click()
        self.driver.find_element_by_xpath('//*[@text="外出打卡"]').click()
        self.driver.find_element_by_xpath('//*[contains(@text,"次外出")]').click()
        #验证
        self.driver.find_element_by_xpath('//*[@text="外出打卡成功"]')


    def wait_for_text(self,text):
        try:
            WebDriverWait(self.driver,5).until(lambda x : x.find_element(MobileBy.XPATH,f"//*[@text='{text}']"))
            return True
        except:
            return False





    def test_deleteMember(self):
        """
        删除联系人:
        点击通讯录
        点击搜索图标，填入搜索内容，计算搜索出来的人数num
        点击一个联系人，进入详情页
        点击右上角的三个点点，进入个人信息页
        点击编辑成员
        网上滑动，点击删除成员
        点击确定，回到搜素结果页，计算搜索出来的人数num2
        验证num-1==num2

        :return:
        """
        searchkey = '金克斯'
        self.driver.find_element_by_xpath('//*[@text="通讯录"]').click()
        #通过点击放大镜
        # self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/kci']").click()
        # 通过查找公司那一个级别的后面的兄弟节点。following-sibling 就是找到当前结点 后面的所有结点,如果找到多个元素，下标从1开始，比如 1,2,3...
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@text='环易网络科技有限公司']/../../../following-sibling::*/*[1]").click()

        #输入搜索词
        self.driver.find_element_by_xpath('//*[@text="搜索"]').send_keys(searchkey)

        exists = self.wait_for_text('联系人')
        #如果没有搜索结果
        if not exists:
            pytest.xfail(reason=f"无搜索结果：{searchkey}")




        #如果有搜索结果，获取联系人下方的个数
        start_elements_size = self.driver.find_elements_by_xpath("//*[@resource-id='com.tencent.wework:id/esq']")


        start_elements_len = len(start_elements_size)

        #点击第一个联系人
        self.driver.find_elements_by_xpath("//*[@resource-id='com.tencent.wework:id/esq']")[0].click()
        #另外一种方法点击联系人第一个
        # self.driver.find_elements_by_xpath(MobileBy.XPATH,"//*[@text='联系人']/../following-sibling::*")[0].click()

        # self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.wework:id/kc8")').click()
        #点击右上角的三个点
        # self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.wework:id/kc8"]').click()

        # 通过找到个人信息的兄弟节点
        self.driver.find_element(MobileBy.XPATH,"//*[@text='个人信息']/../../../../following-sibling::*[1]").click()

        self.driver.find_element_by_xpath('//*[@text="编辑成员"]').click()
        self.driver.find_element_by_xpath('//*[@text="部门"]').click()

        self.swipe_find(3,'删除成员').click()
        self.driver.find_element_by_xpath('//*[@text="确定"]').click()
        #获取删除后的联系人个数
        end_elements_size = self.driver.find_elements_by_xpath("//*[@resource-id='com.tencent.wework:id/esq']")

        end_elements_len = len(end_elements_size)
        assert start_elements_len-1 == end_elements_len

        # search_locator = (By.ID,'***')
        # WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(search_locator))
        # self.driver.find_element(*search_locator).click()

        # #切换上下文
        # self.driver.switch_to.context(self.driver.contexts[-1])

        #切换窗口
        # self.driver.switch_to.window(self.driver.window_handles[-1])



































