from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWX():
    def setup(self):
        desire_caps = {}
        desire_caps['platformName'] = 'Android'
        desire_caps['deviceName'] = 'AAA'
        desire_caps['appPackage'] = 'com.tencent.wework'
        desire_caps["appActivity"] = '.launch.WwMainActivity'
        desire_caps["noReset"] = 'True'
        # 最重要的代码，建立客户端与服务端的连接
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()


    def test_delete_contact(self):
        # 点击通讯录
        self.driver.find_element_by_xpath('//*[@text="通讯录"]').click()
        # 点击搜索按钮
        self.driver.find_element_by_id('com.tencent.wework:id/i6n').click()
        # 在搜索框中输入要删除的成员
        self.driver.find_element_by_xpath('//*[@text="搜索"]').send_keys("测试")
        # 获取界面成员个数
        con_num1 = self.driver.find_elements_by_id("com.tencent.wework:id/dns")
        # con_num1 = self.driver.find_elements(MobileBy.ANDROID_UIAUTOMATOR,
        #                                  'new UiScrollable(new UiSelector()'
        #                                  '.scrollable(true).instance(0))'
        #                                  '.scrollIntoView(new UiSelector()'
        #                                  '.resourceId("com.tencent.wework:id/dns").instance(0));')
        before_delete = len(con_num1)
        print(before_delete)
        # 判断是否有成员可以删除
        if before_delete < 1:
            print("没有可以删除的成员")
            return
        # 点击要删除的成员
        con_num1[0].click()
        # 点击更多选项
        self.driver.find_element_by_id("com.tencent.wework:id/i6d").click()
        # 点击编辑成员
        self.driver.find_element_by_xpath('//*[@text="编辑成员"]').click()
        # 点击删除成员
        self.driver.find_element_by_xpath('//*[@text="删除成员"]').click()
        # 点击确定
        self.driver.find_element_by_xpath('//*[@text="确定"]').click()
        # 获取界面成员个数
        con_num2 = self.driver.find_elements_by_id("com.tencent.wework:id/dns")
        # con_num2 = self.driver.find_elements(MobileBy.ANDROID_UIAUTOMATOR,
        #                                  'new UiScrollable(new UiSelector()'
        #                                  '.scrollable(true).instance(0))'
        #                                  '.scrollIntoView(new UiSelector()'
        #                                  '.resourceId("com.tencent.wework:id/dns").instance(0));')

        after_delete = len(con_num2)
        print(after_delete)
        # 断言判断
        assert after_delete == before_delete - 1



