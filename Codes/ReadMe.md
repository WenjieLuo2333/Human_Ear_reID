All the dataset path are deleted. The path are shown in './data_set_structure.png'
In fact all you need to download is [re_image],[resized_cropped_detection] and [resized_detection_2] in order to test the models.

All the path except Ear_Verification are Empyty
All these annotations and datasets can downloaded from https://drive.google.com/drive/folders/1YwM0I2ulZUcrwt95GTf_nW9qIrH9PklR?usp=sharing

The main part is loacated in './Ear_Verification', 
And this part is for data preparation.You dont have to run any script in this path.

Please check the readme in './Ear_Verification'

annotations are annotation for original images
cropped_GT are cropped ears from ground truth
cropped_detection are detected ears
resized_cropped_detection are deteced ears resized into 224*224 with worse model.
detection_2 are detected ears by better model
resized_detection_2 are detected ears by better model resized into 224*224
re_ano are annotations for images resized into 960*680
re_image are images resized into 960*680


To reproduce the test part, you only need to download the re_image,resized_cropped_detection and resized_detection_2.


resized_detection.py are used to resize detected images.[You dont have to run]
make easy_pair and make_train_pair are used to generate training pairs. [You dont have to run]
check_annotation.ipynb is used to convert annotation from origin size to 960*680 size.[You dont have to run]
Get_Train.ipynb is used check training data.[You dont have to run]
RCNN.ipynb is used to generate annotate.txt