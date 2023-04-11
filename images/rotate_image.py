# -*- coding:utf-8 -*-
from PIL import Image

# 图片转向


def rotate_image(image_path, output_path):
	with Image.open(image_path) as image:
		if image.width > image.height:
			# 横图，需要旋转
			rotated_image = image.transpose(method=Image.ROTATE_270)
			rotated_image.save(output_path)
		else:
			# 竖图，不需要操作
			image.save(output_path)


# 示例用法
image_path = "/Users/tanglingxiao/Downloads/temp/in/WechatIMG8.jpeg"
output_path = "/Users/tanglingxiao/Downloads/temp/out/WechatIMG8.jpeg"
rotate_image(image_path, output_path)
