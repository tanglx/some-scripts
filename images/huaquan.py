# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('img.png')  # 读取图片
cv2.circle(img, (1277, 2033), 50, (0, 0, 255), 20)
# plt.subplot(2, 2, 1)  # 两行两列 位置为1
plt.imshow(img)
plt.axis('off')  # 关闭坐标轴
plt.title('Img1.png')
plt.show()

# cv2.imwrite("./out.png", img)


