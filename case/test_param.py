# -*- coding: UTF-8 -*-
import unittest
from parameterized import parameterized
class TestPara(unittest.TestCase):
    @parameterized.expand([("admin","12345"),("user002","654321")])
    def test_para(self,username,password):
        print (username)
        print (password)