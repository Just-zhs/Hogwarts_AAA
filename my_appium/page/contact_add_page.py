from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from my_appium.page.base_page import BasePage

'''
编辑联系人页面
'''


class ContactAddPage(BasePage):
    def edit_contact(self, name, gender, phonenum):
        '''
        编辑成员信息
        '''
        self.find(MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText').send_keys(
            name)
        self.find(MobileBy.XPATH, "//*[@text='性别']/..//*[@text='男']").click()
        if gender == "男":
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='女']"))
            self.find(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.find(MobileBy.XPATH, "//*[@text='女']").click()

        self.find(MobileBy.XPATH, "//*[@text='手机号']").send_keys(phonenum)
        self.find(MobileBy.XPATH, "//*[@text='保存']").click()

        from my_appium.page.menber_invite_page import MenberInviteMenuPage
        return MenberInviteMenuPage(self.driver)

    def delete_contact(self):
        self.find(MobileBy.XPATH, '//*[@text="删除成员"]').click()
        self.find(MobileBy.XPATH, "//*[@text='确定']").click()
        from my_appium.page.menber_search_page import MemberSearchPage
        return MemberSearchPage(self.driver)
