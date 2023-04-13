# -*- coding:utf-8 -*-
import requests
url = "http://map.baidu.com/?qt=bsi&c=75"
resp = requests.get(url).text
print(resp)
