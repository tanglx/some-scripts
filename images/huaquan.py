# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt


image = plt.imread('./img.png')
plt.title('Read Image by Matplotlib')
plt.axis('off')

plt.imshow(image)
plt.show()


