from PIL import Image
import numpy as np
import cv2, time, pexif, os

start_ts = time.time()

img_path = "/Users/alex/Desktop/Projects/Mustard/Images/test.JPG"

# orientation = pexif.JpegFile.fromFile(img_path)
# orientation.exif.primary.Orientation[0] = 1

os.system("exiftool -Orientation=1 -n " + img_path)

img = cv2.imread(img_path)
Z = img.reshape((-1,3))

img2 = Image.open(img_path)
img2 = img2.convert("RGBA")

input_size = img2.size
# print(input_size)
Z = np.float32(Z)
result = np.float32(np.dot(Z, [[0.21], [0.72], [0.07]]))
# print(result)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 2

ret,label,center=cv2.kmeans(result,K,None,criteria,3,cv2.KMEANS_RANDOM_CENTERS)

newData = []
for i in label.flatten():
	if i == 0:
		newData.append((255, 255, 255, 0))
	else:	
		newData.append((0, 0, 0, 255))

output_img = Image.new("RGBA", (input_size[0], input_size[1]))
output_img.putdata(newData)
output_img.save("output.png", "PNG")

end_ts = time.time()
print(end_ts - start_ts)
print("---------------------------------------------------------")