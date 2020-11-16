from appium.webdriver.common.mobileby import MobileBy

from my_appium.page.base_page import BasePage


class MemberInfPage(BasePage):
    """
    个人信息页面
    """
    def more(self):
        self.find(MobileBy.ID, "com.tencent.wework:id/i6d").click()
        return self

    def edit_member(self):
        # 点击【编辑成员】
        self.find(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        from my_appium.page.contact_add_page import ContactAddPage
        return ContactAddPage(self.driver)