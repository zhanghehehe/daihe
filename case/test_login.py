# -*- coding: UTF-8 -*-
import unittest
from api.api_login import ApiLogin:
class TestLogin(unittest.TestCase):
    def test_login(self):
        url = "www.baidu.com"
        mobile = "18201019342"
        code = "12345"
        res = ApiLogin().api_post_login(url,mobile,code)
        self.assertEquals("ok",res.json()["message"])
        self.assertEquals(201,res.status_code)
        self.a
if __name__== '__main__':
    unittest.main()

