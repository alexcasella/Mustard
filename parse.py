from PIL import Image
import numpy as np
import cv2
import time

start_ts = time.time()

img = cv2.imread("/Users/alex/Desktop/Projects/Mustard/Images/test.JPG")
Z = img.reshape((-1,3))

img2 = Image.open('/Users/alex/Desktop/Projects/Mustard/Images/test.JPG')
img2 = img2.convert("RGBA")


# convert to np.float32
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 2

ret,label,center=cv2.kmeans(Z,K,None,criteria,3,cv2.KMEANS_RANDOM_CENTERS)

# print("++++++++++++++ RET ++++++++++++++++++")
# print(ret)
print("++++++++++++++ LABEL ++++++++++++++++++")
print(label)
print("++++++++++++++ CENTER ++++++++++++++++++")
print(center)

newData = []
print(center[0][0], center[0][1], center[0][2])

print(label.flatten())
print("-----------------------------------------------------")

for i in label.flatten():
	if i == 1:
		newData.append((255, 255, 255, 0))
	else:	
		newData.append((center[i][0], center[i][1], center[i][2], 255))

img2.putdata(newData)
img2.save("img1.png", "PNG")

end_ts = time.time()
print(end_ts - start_ts)





