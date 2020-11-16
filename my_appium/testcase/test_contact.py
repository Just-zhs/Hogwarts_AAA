from time import sleep

import pytest

from my_appium.page.app import App


class TestWX:
    def setup_class(self):
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main()

    def teardown_class(self):
        self.app.stop()


    def test_addcontact(self):
        name = "hogwarts_00005"
        gender = "男"
        phonenum = "13812121225"


        result = self.main.goto_contact(). \
            add_member().add_member_manul(). \
            edit_contact(name, gender, phonenum).verify_toast()
        assert '添加成功' == result

    def test_addcontact1(self):
        name = "hogwarts_00003"
        gender = "男"
        phonenum = "13812121214"

        result = self.main.goto_contact(). \
            add_member().add_member_manul(). \
            edit_contact(name, gender, phonenum).verify_toast()
        assert '添加成功' == result

    def test_delete_memebr(self):
        name = "hogwarts"
        action1 = self.main.goto_contact().search_member().input_member(name)
        num1 = action1.get_number()
        # 判断是否有成员可以删除
        if num1 < 1:
            print("没有可以删除的成员")
            return
        action2 = action1.get_member().more().edit_member().delete_contact()
        sleep(2)
        num2 = action2.get_number()
        assert num1 == num2 + 1


