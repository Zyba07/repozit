import os 
import cv2
import numpy as np
image_path = r'test_data\imagesfd.png'
image = cv2.imread(image_path)
print(image.shape)
img =image
img_width, img_height, img_channels = img.shape

def chess_desk_img (img_path, w_divider, h_divider):
    img_width == img_height
    img = cv2.imread(img_path)
    x_step = int(img_width / w_divider)
    y_step = int(img_height / h_divider)
    current_x = 0
    current_y = 0

    for i in range(h_divider):
        previous_y = current_y
        current_y += y_step
        current_x = 0
        for j in range(w_divider):
            previous_x = current_x
            current_x += x_step
            preprevious_x = previous_x - x_step
            if i%2 == 0 and j%2 != 0:
                crop = img[previous_y:current_y,previous_x:current_x,:]
                crop *= 0
            elif i%2 != 0 and j%2 != 0:
                crop = img[previous_y:current_y,preprevious_x:previous_x,:]
                crop *= 0
    return img

chess_desk = chess_desk_img('vse_podryad\imagesfd.png', 40, 10),
cv2.imshow('voblya', chess_desk)
cv2.waitKey(-1)




