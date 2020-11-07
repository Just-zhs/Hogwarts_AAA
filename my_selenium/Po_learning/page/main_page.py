from selenium.webdriver.common.by import By

from my_selenium.Po_learning.page.base_page import BasePage
from my_selenium.Po_learning.page.add_contacts_page import AddContactsPage


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def add_contacts(self):
        self.find(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        return AddContactsPage(self.driver)
