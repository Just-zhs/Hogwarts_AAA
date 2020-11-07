from my_selenium.Po_learning.page.main_page import MainPage
import my_selenium.func as fc

class TestContact:
    def setup(self):
        # 生成新对象和测试数据
        self.main = MainPage()
        self.name = fc.name_gener()
        self.account = fc.account_gener()
        self.number = fc.number_gener()

    def test_addcontact(self):
        # 页面return到add_contacts_page页面
        addcontact = self.main.add_contacts()
        # 调用add_contacts_page页面方法
        addcontact.add_contact(self.name, self.account, self.number)
        res = addcontact.get_contacts(self.name)
        assert res
