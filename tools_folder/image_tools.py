#py welcome_to_image.py

import os
import cv2
import numpy as np
from varname.helpers import debug
img_path = 'papkaPY\Zyba07\data_analys_code\testdata\crazy-frog-racer-4e2647bb7576d.jpg'
debug(img_path)
img = cv2.imread(img_path)
img2draw = img.copy()
img2draw = cv2.resize(img2draw, dsize=None, fx=0.5, fy=0.5)
debug(img.shape)
img_height, img_width, img_channels = img2draw.shape
debug(img_height)
debug(img_width)
img_center_xy = (int(img_width/2), int(img_height/2))
w_divider = 10
h_divider = 10
x_step = int(img_width/w_divider)
y_step = int(img_height/h_divider)
current_x = 0
current_y = 0
for x_step_id in range(w_divider):
    previous_x = current_x
    current_x += x_step
    for y_step_id in range(h_divider):
        previous_y = current_y
        current_y += y_step
        crop = img2draw[previous_y:current_y, previous_x:current_x, :]
        # cv2.imshow('porezali', crop)
        # cv2.waitKey(2)
        img2draw = cv2.rectangle(img2draw, pt1=(previous_x, previous_y), pt2=(current_x, current_y), color=(0, 0, 200), thickness=2)
    current_y = 0

for i in range(20):
    img2draw = cv2.circle(img2draw, center=img_center_xy, radius=int(2*np.e*i), color=(0, 200, 0), thickness=2 )

cv2.imshow('papkaPY\Zyba07\data_analys_code\testdata\crazy-frog-racer-4e2647bb7576d.jpg', img2draw)
cv2.waitKey(-1) 