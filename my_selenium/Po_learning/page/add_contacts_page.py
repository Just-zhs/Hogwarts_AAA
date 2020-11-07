from selenium.webdriver.common.by import By

from my_selenium.Po_learning.page.base_page import BasePage


class AddContactsPage(BasePage):

    def add_contact(self, name, account, num):
        self.find(By.ID, 'username').send_keys(name)
        self.find(By.ID, 'memberAdd_acctid').send_keys(account)
        self.find(By.ID, 'memberAdd_phone').send_keys(num)
        # 保存
        self.find(By.XPATH,
                  '/html/body/div[1]/div/div/main/div/div/div[2]/div/div[4]/div/form/div[1]/a[2]').click()
        return True

    def get_contacts(self, value):
        # 当勾选框可点击时，开始获取信息
        locator = (By.CSS_SELECTOR, ".ww_checkbox")
        self.wait_for_click(locator)

        titles_total = []
        while True:
            elements = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
            titles = [element.get_attribute("title") for element in elements]
            if value in titles:
                return True
            titles_total.extend(titles)

            page: str = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
            num, total = page.split("/", 1)

            if int(num) == int(total):
                return False
            else:
                self.find(By.CSS_SELECTOR, ".ww_commonImg_PageNavArrowRightNormal").click()

        return titles_total

