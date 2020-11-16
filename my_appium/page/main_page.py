from appium.webdriver.common.mobileby import MobileBy

from my_appium.page.base_page import BasePage
from my_appium.page.contact_page import ContactPage


class MainPage(BasePage):
    _contact_list = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_contact(self):
        '''
        进入到通讯录
        '''
        # 点击【通讯录】


        # *解元组
        self.find(*self._contact_list).click()
        return ContactPage(self.driver)