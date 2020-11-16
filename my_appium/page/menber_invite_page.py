from appium.webdriver.common.mobileby import MobileBy

from my_appium.page.base_page import BasePage


class MenberInviteMenuPage(BasePage):
    def add_member_manul(self):
        # 点击【手动输入添加】
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        from my_appium.page.contact_add_page import ContactAddPage
        return ContactAddPage(self.driver)

    def verify_toast(self):
        # result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        result = self.get_toast_text()
        return result