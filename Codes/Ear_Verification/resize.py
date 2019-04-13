import cv2
import os
import numpy as np
lis = os.listdir('./test')
for i in lis:
	img = cv2.imread('./test/'+i)
	newimg = cv2.resize(img,(int(680),int(960)))
	newimg = np.rot90(newimg)
	cv2.imwrite('./test/'+i,newimg)