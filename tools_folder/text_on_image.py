import cv2
import numpy as np

def add_info_to_image(img_path):
    image = cv2.imread(img_path)
    re_image = image
    re_image = cv2.resize(re_image, dsize=None, fx=0.7, fy=0.7)
    height, width, channels = re_image.shape
    print(height, width, channels)
    info_field = np.zeros(shape=(int(height/8), width, channels), dtype=re_image.dtype)
    cv2.putText(
        img=info_field,
        text=img_path,
        org=(10, 20),
        fontFace=cv2.FONT_HERSHEY_PLAIN,
        fontScale=2,
        color=(0,255,240),
        thickness=1
    )
    
    resolution_str = 'Height::{} Width::{} Channels::{}'.format(height, width, channels)
    
    cv2.putText(
        img=info_field,
        text=resolution_str,
        org=(10, 65),
        fontFace=cv2.FONT_HERSHEY_PLAIN,
        fontScale=2,
        color=(15,255,250),
        thickness=1
    )
    
    image_with_info = np.vstack([info_field, re_image])
    cv2.imshow('result', image_with_info)
    cv2.waitKey(-1)
      
img_path = 'test_data\crazy_frog.png'
add_info_to_image(img_path)
