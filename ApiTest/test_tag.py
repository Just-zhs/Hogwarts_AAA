import json

import pytest
import requests

# todo: 代码冗余
# todo: 与底层框架耦合太多
# todo: 封装层次不足，不利于管理
from ApiTest.tag import Tag


class TestTag:
    def setup_class(self):
        self.tag = Tag()
        self.tag.get_token()
        # 数据清理的过程，把测试数据清空或者还原
        r = self.tag.list()
        for dirty_data in r.json()["tag_group"]:
            print(dirty_data['group_id'])
            self.tag.delete(group_id=dirty_data['group_id'])


    def test_tag_list(self):
        r = self.tag.list()
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    @pytest.mark.parametrize("group_name, tag_names", [
        ["group_demo_1201", [{'name': 'tag_demo_1201'}]],
        ["group_demo_1202", [{'name': 'tag_demo_1202'}, {'name': 'tag_demo_1203'}]],
    ])
    # 测试添加标签
    def test_tag_add(self, group_name, tag_names):
        r = self.tag.add(group_name, tag_names)
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

        r = self.tag.list()
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

        group = [group for group in r.json()['tag_group'] if group['group_name'] == group_name][0]
        tags = [{'name': tag['name']} for tag in group['tag']]
        # print(group)
        # group返回了一个字典
        # print(tags)
        # tags返回了一个列表，列表中是字典
        assert group['group_name'] == group_name
        assert tags == tag_names

    # 测试空标签
    def test_add_empty1(self):
        r = self.tag.add("", "")
        print(r.json())
        assert r.status_code == 200
        assert r.json()["errcode"] == 40063

    # 测试空tagname
    def test_add_empty2(self):
        r = self.tag.add("123", [{'name': ''}])
        print(r.json())
        assert r.status_code == 200
        assert r.json()["errcode"] == 41018

    @pytest.mark.parametrize("group_name, tag_names", [
        ["group_demo_1201", [{'name': 'tag_demo_1201'}]]])
    # group_name和tag_name已存在,测试重复情况
    def test_tag_add_fail1(self, group_name, tag_names):
        # 获取当前标签
        data = self.tag.list()
        # 判断当前内容是否为空
        if data.json()["tag_group"] == []:
            self.tag.add(group_name, tag_names)
            r = self.tag.add(group_name, tag_names)
        else:
            group = data.json()["tag_group"][0]["group_name"]
            tag = data.json()["tag_group"][0]["tag"][0]["name"]
            print(group)
            print(tag)
            r = self.tag.add(group, [{'name': tag}])

        assert r.status_code == 200
        assert r.json()['errcode'] == 40071

    @pytest.mark.parametrize("group_name, tag_names", [
        ["1111112222255555111112222255555", [{'name': 'tagname1'}]],
        ["fail_demo2", [{'name': '1111112222255555111112222255555'}]]
    ])
    # 用例1为group_name 超过30个字符
    # 用例2为tag_name 超过30个字符
    def test_tag_add_fail2(self, group_name, tag_names):
        r = self.tag.add(group_name, tag_names)
        # print(r.json())
        assert r.status_code == 200
        assert r.json()['errcode'] == 40058

    # 删除tag
    def test_tag_delete_tag(self):
        data = self.tag.list()
        # 判断当前内容是否为空
        if data.json()["tag_group"] == []:
            print("没有数据可删除")
        else:
            tag_id = data.json()["tag_group"][0]["tag"][0]["id"]
            r = self.tag.delete(tag_id=[tag_id])
            print(r.json())
            assert r.status_code == 200
            assert r.json()['errcode'] == 0

    # 删除group
    def test_tag_delete_group(self):
        data = self.tag.list()
        # 判断当前内容是否为空
        if data.json()["tag_group"] == []:
            print("没有数据可删除")
        else:
            group_id = data.json()["tag_group"][0]["group_id"]
            r = self.tag.delete(group_id=[group_id])
            print(r.json())
            assert r.status_code == 200
            assert r.json()['errcode'] == 0

    # 测试group_id，tag_id都传空值
    def test_tag_delete_empty(self):
        data = self.tag.list()
        # 判断当前内容是否为空
        if data.json()["tag_group"] == []:
            print("没有数据可删除")
        else:
            r = self.tag.delete()
            print(r.json())
            assert r.status_code == 200
            assert r.json()['errcode'] == 41017

# todo: 课后作业：丰富标签管理的测试用例，主要是list add delete接口，拔高点完善下数据清理的过程
