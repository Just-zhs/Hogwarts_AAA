import shelve
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from my_selenium.func import name_gener, account_gener, number_gener


class TestWX:
    def setup(self):
        # 复用浏览器
        # option = Options()
        # option.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    '''
    def test_get_cookie(self):
        # 复用浏览器get_cookie
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        cookies = self.driver.get_cookies()
        print(cookies)
    '''

    '''
    def test_add_cookies(self):
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688853100070385'},
            {'domain': '.qq.com', 'expiry': 1910567821, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
             'secure': False, 'value': '0_5f14f08cca1e5'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1636029094, 'httpOnly': False,
             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1604493094'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'NYbKSIWUmtWAfN24xT_hhlmvp7oRaXECTubW6uJk1IQA5OgOszGWxX_HKLth3nVyR3Ad74UYl0YCtx7Tn9_JGCOJpmrL_L3BCKQRYmd3ZGa4UY0qAOXb--ES9EWma1Bf0rKW_ZxJLKyNwZxPkQtglz3No2ymemmWVBcOr3M6BYEJJ_L3eckb5dTa35MfOutUqWDrH5VQV8vcjlCo1axxNhzJ5XxvnMYliOIerkZ1nWDJ0lO6_o7hNbLtZih2P9flNSjvACDLg1q8i2kR9iNZ3g'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688853100070385'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '2671518720'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '5233905074'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325073176027'},
            {'domain': '.qq.com', 'expiry': 1604587473, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.1317917140.1604493095'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'HuThcVXoiLbHxZICQxrlw4NHhCQ49Dp-P385e2det1nWMXKXxVOdpwVzezFguAn2'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a4469133'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '0264249'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1607093093, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.qq.com', 'expiry': 1667573073, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1527110851.1604493095'},
            {'domain': '.qq.com', 'expiry': 1904451657, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
             'secure': False, 'value': '526d7ae436842284'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1636028869, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 1606797057, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/',
             'secure': False, 'value': '541236205'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 1621748192, 'httpOnly': False, 'name': 'eas_sid', 'path': '/',
             'secure': False, 'value': 'l165A9f0L2Q1p2a1d9t2O2H8P6'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': '9007b6f2ebcf1f42e526ec3b7c8d5f7ad00ffe702afb9be8375246e62dfd21f4'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1604524405, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '8lbsj8t'},
            {'domain': '.qq.com', 'expiry': 1604501102, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'FLZEPMyiY1'}]

        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.refresh()
    '''

    '''
    def test_case(self):
        # 向shelve里存放数据
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688853100070385'},
            {'domain': '.qq.com', 'expiry': 1910567821, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
             'secure': False, 'value': '0_5f14f08cca1e5'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1636029094, 'httpOnly': False,
             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1604493094'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'NYbKSIWUmtWAfN24xT_hhlmvp7oRaXECTubW6uJk1IQA5OgOszGWxX_HKLth3nVyR3Ad74UYl0YCtx7Tn9_JGCOJpmrL_L3BCKQRYmd3ZGa4UY0qAOXb--ES9EWma1Bf0rKW_ZxJLKyNwZxPkQtglz3No2ymemmWVBcOr3M6BYEJJ_L3eckb5dTa35MfOutUqWDrH5VQV8vcjlCo1axxNhzJ5XxvnMYliOIerkZ1nWDJ0lO6_o7hNbLtZih2P9flNSjvACDLg1q8i2kR9iNZ3g'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688853100070385'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '2671518720'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '5233905074'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325073176027'},
            {'domain': '.qq.com', 'expiry': 1604587473, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.1317917140.1604493095'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'HuThcVXoiLbHxZICQxrlw4NHhCQ49Dp-P385e2det1nWMXKXxVOdpwVzezFguAn2'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a4469133'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '0264249'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1607093093, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.qq.com', 'expiry': 1667573073, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1527110851.1604493095'},
            {'domain': '.qq.com', 'expiry': 1904451657, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
             'secure': False, 'value': '526d7ae436842284'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1636028869, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 1606797057, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/',
             'secure': False, 'value': '541236205'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 1621748192, 'httpOnly': False, 'name': 'eas_sid', 'path': '/',
             'secure': False, 'value': 'l165A9f0L2Q1p2a1d9t2O2H8P6'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': '9007b6f2ebcf1f42e526ec3b7c8d5f7ad00ffe702afb9be8375246e62dfd21f4'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1604524405, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '8lbsj8t'},
            {'domain': '.qq.com', 'expiry': 1604501102, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'FLZEPMyiY1'}]
        db = shelve.open('cookies')
        db['cookie'] = cookies
        db.close()
    '''

    def test_add_contacts(self):
        # shelve 模块， python 自带的对象持久化存储
        db = shelve.open('cookies')
        cookies = db['cookie']
        db.close()
        # 打开无痕新页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 加入cookie
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        # 刷新页面获取登录状态
        self.driver.refresh()
        # 生成联系人测试数据
        name = name_gener()
        account = account_gener()
        num = number_gener()
        # 点击添加联系人
        self.driver.find_element_by_css_selector('.index_service_cnt_itemWrap:nth-child(1)').click()
        # 输入信息
        self.driver.find_element_by_id('username').send_keys(name)
        self.driver.find_element_by_id('memberAdd_acctid').send_keys(account)
        self.driver.find_element_by_id('memberAdd_phone').send_keys(num)
        # 点击保存
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div/div[2]/div/div[4]/div/form/div[1]/a[2]').click()
        # 抓取保存成功的提示作为断言的判断
        tips = self.driver.find_element_by_xpath('//*[@id="js_tips"]').text
        assert '保存成功' == tips




if __name__ == '__main__':
    pytest.main(['-s'],['-v'])

# pytest test_wx.py  --alluredir=./result/1
