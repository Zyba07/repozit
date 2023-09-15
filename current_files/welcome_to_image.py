
import os
import cv2
import numpy as np
from varname.helpers import debug


img_path = ('c:/cod/repozit_001/test_data\medved.jpg')
debug(img_path)
img = cv2.imread(img_path)
img2draw =img.copy()
img2draw = cv2.resize(img2draw, dsize=None, fx=0.5, fy=0.5)
debug(img.shape)
img_height, img_width, img_channels =img2draw.shape
debug(img_height)
debug(img_width)
img_centr_xy = (int(img_width/2), int(img_height/2))
debug(img_centr_xy)
img2draw = cv2.circle(img2draw, center=(172, 307), radius=50, color=(0, 200, 0), thickness=3 )#рисуем круг

cv2.imshow('medved.jpg', img2draw)
cv2.waitKey(-1)




# print(img_width)
# img_top1 = img[:100,:,:]
# out_path = 'top_jeesus1.jpg'
# cv2.imwrite(out_path, img_top1)
# # print('written  to ', out_path)
# img_left = img[:,200:400,:]
# out_path = 'jeesus_left.jpg'
# cv2.imwrite(out_path, img_left)
# # print('written  to ', out_path)
# img_centr = img[350:450,250:450,:]
# out_path = 'img_centr.jpg'
# cv2.imwrite(out_path, img_centr)
# # print('written  to ', out_path)

