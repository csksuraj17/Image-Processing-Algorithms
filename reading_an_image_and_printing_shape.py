import cv2 
import glob
for i in glob.glob("im.jpg"):
	img = cv2.imread(i)  
print(img.shape)

