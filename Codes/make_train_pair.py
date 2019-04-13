import numpy as np
import pandas as pd
import os
import random
image_path = '/home/wenjie/Desktop/earImageDataset/cropped_GT'
aft = ['_','_d','_dt','_t']
idx = [('%03d'%i) for i in range(1,196)];
sample_num = 1000;

f = open('./positive_pairs.txt','w')
for j in range(8):
	for i in range(195):
		valid = random.sample(aft,3)
		tmps = idx[i] + valid[0] + '.jpg,' + idx[i] + valid[1] + '.jpg,' + idx[i] + valid[2] + '.jpg,1\n'
		f.write(tmps)
f.close()


f = open('./negative_pairs.txt','w')
for j in range(8):
	for i in range(195):
		valid = random.sample(aft,2)
		test = random.sample(aft,1)[0]
		test_im = random.sample(idx,1)[0]
		if test_im == idx[i]:
			continue
		tmps = idx[i] + valid[0] + '.jpg,' + idx[i] + valid[1] + '.jpg,' + test_im + test + '.jpg,0\n'
		f.write(tmps)
f.close()