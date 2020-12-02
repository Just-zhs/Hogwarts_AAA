import json

import requests

corpid = 'ww07073dfd26e0cedf'
corpsecret = 'VFMP3JPo9jfmnR1KW98uWKTaj_p-K9-nFC8HIdqVChg'


class Tag:
    def __init__(self):
        self.token = ""

    def get_token(self):
        # 获取token
        r = requests.get(url='https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                         params={"corpid": corpid, "corpsecret": corpsecret})
        # print(json.dumps(r.json(), indent=2))
        # 函数内使用的变量可以用self传递，不需要return
        self.token = r.json()["access_token"]

    def list(self):
        r = requests.post(url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
                          params={"access_token": self.token},
                          json={"tag_id": []})
        # print(json.dumps(r.json(), indent=2))
        # 这个返回r，方便testcase中r.status_code等判断
        return r

    def add(self, group_name, tag_name):
        r = requests.post(url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
                          params={"access_token": self.token},
                          json={
                              "group_name": group_name, "tag": tag_name
                          }
                          )
        # print(json.dumps(r.json(), indent=2))
        return r

    def delete(self, tag_id=[], group_id=[]):
        r = requests.post(url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
                          params={"access_token": self.token},
                          json={
                              "tag_id": tag_id,
                              "group_id": group_id
                          }
                          )
        # print(json.dumps(r.json(), indent=2))
        return r


if __name__ == '__main__':
    Api = Tag()
    Api.get_token()
