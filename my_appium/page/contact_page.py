from appium.webdriver.common.mobileby import MobileBy

from my_appium.page.menber_invite_page import MenberInviteMenuPage
from my_appium.page.base_page import BasePage
from my_appium.page.menber_search_page import MemberSearchPage


class ContactPage(BasePage):
    def add_member(self):
        self.find_by_scroll("添加成员").click()
        return MenberInviteMenuPage(self.driver)

    def search_member(self):
        self.find(MobileBy.ID, "com.tencent.wework:id/i6n").click()
        return MemberSearchPage(self.driver)
