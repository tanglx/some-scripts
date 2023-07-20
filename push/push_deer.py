# -*- coding:utf-8 -*-
import time

# 推送
from pypushdeer import PushDeer

push_deer = PushDeer(server="http://140.210.211.157:8800", pushkey="PDU1T32oq6sqNvZk5K7ygSQH0jQBPjwRCe2Ij")


def push_text(title, content):
    push_deer.send_text(title, desp=content)
    # pushdeer.send_markdown("# hello world", desp="**optional** description in markdown")
    # push_deer.send_image("https://github.com/easychen/pushdeer/raw/main/doc/image/clipcode.png")
    # pushdeer.send_image(
    #     "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVQYV2NgYAAAAAMAAWgmWQ0AAAAASUVORK5CYII=")


if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    push_text("标题：" + now, "内容：" + now)
