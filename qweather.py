# -*- coding:utf-8 -*-
import json
import requests
import logging as log
import push


key = "217533b7c4fe459b9d41870df4e37916"
url = "https://devapi.qweather.com/v7/weather/now?location=101010100&key=" + key

r = requests.get(url)
if r.status_code != 200:
    log.error("error")
info = json.loads(r.content.decode())

now = info["now"]
push.push_deer.push_text("天气", now)
