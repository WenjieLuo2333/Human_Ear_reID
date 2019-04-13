import numpy as np
import os
import cv2
img_path = './detection_2'
out_path = './resized_detection_2'
imgs = os.listdir(img_path)
for img in imgs:
	img_ = cv2.imread(img_path + '/' + img)
	newimg = cv2.resize(img_,(int(224),int(224)))
	cv2.imwrite(out_path + '/' + img,newimg)
