# -*- coding: UTF-8 -*-
import unittest
import json
import requests
url="http://123.57.26.252:8162/jyfq-mapi/contract/repair"
json={
  "orderDetailId":"552531457014694657",
  "contractTypes":["CA","wtdksqs"]
     }
re = requests.post(url,json)
res = re.content
print (res)