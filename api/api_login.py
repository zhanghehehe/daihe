# -*- coding: UTF-8 -*-
import requests
class ApiLogin(object):
    def api_post_login(self,url,mobile,code):
        headers = {"content-Type":"application/json"}
        data = {"mobile":mobile,"code":code}
        return requests.post(url,headers=headers,json=data)