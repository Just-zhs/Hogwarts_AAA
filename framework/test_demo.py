import re

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.get_log import log

def load_data(path):
    # 从yaml文件家在数据
    with open(path, encoding='utf-8') as f:
        return yaml.safe_load(f)


def test_load_data():
    print(load_data("test_data.yaml"))


class TestDemo():
    @pytest.mark.parametrize('data', load_data("test_data.yaml")['data']
                             )
    def test_search(self, data):

        for step in load_data("test_data.yaml")['steps']:
            if "webdriver" in step:
                log.info("开始启动浏览器")
                browser = str(step.get("webdriver").get("browser", "chrome")).lower()
                # get中第二个参数为默认值，如果值为空取chrome
                if browser == 'chrome':
                    driver = webdriver.Chrome()
                    log.info("启动chrome浏览器成功")
                elif browser == 'firefox':
                    driver = webdriver.Firefox()
                    log.info("启动firefox浏览器成功")
                else:
                    print(f"{driver} don't know which browser")


            if 'get' in step:
                url = step.get('get')
                driver.get(url)
                log.info(f"获取地址{url}")


            if 'find_element' in step:
                if isinstance(step.get('find_element'), list):
                    by = step.get('find_element')[0]
                    locator = step.get('find_element')[1]

                elif isinstance(step.get('find_element'), dict):
                    by = step.get('find_element')['by']
                    locator = step.get('find_element')['value']
                current_element = driver.find_element(by, locator)
                log.info(f"查找元素{by} {locator}")


            if 'click' in step:
                current_element.click()
                log.info("点击")


            if 'send_keys' in step:
                value = str(step.get('send_keys'))
                print(value)
                # 判断value是否为变量
                """
                # 使用正则匹配
                # if re.search('\$\{data\}',value):
                """
                # 直接匹配
                if value == '${data}':
                    value = value.replace('${data}', data)
                    current_element.send_keys(value)
                    log.info(f"输入{value}")
