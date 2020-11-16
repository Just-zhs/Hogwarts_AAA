from appium.webdriver.common.mobileby import MobileBy

from my_appium.page.base_page import BasePage
from my_appium.page.menber_inf_page import MemberInfPage


class MemberSearchPage(BasePage):
    """
    进入成员搜索界面
    """
    def input_member(self,name):
        self.find(MobileBy.XPATH, '//*[@text="搜索"]').send_keys(name)
        return self




    def get_number(self):
        con_num1 = self.find_elements(MobileBy.ID, "com.tencent.wework:id/dns")
        num = len(con_num1)
        print(num)

        return num

    def get_member(self):
        con_num1 = self.find_elements(MobileBy.ID, "com.tencent.wework:id/dns")
        num = len(con_num1)
        print(num)
        # 点击要删除的成员
        con_num1[0].click()
        return MemberInfPage(self.driver)