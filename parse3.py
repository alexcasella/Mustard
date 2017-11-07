import os
import time
import pexif
from PIL import Image
import numpy as np

start_ts = time.time()


# get image and fix orientation
img_path = "/Images/sig.JPG"
os.system("exiftool -Orientation=1 -n " + img_path)


# parse image into simple array
pil_img = Image.open(img_path)
rawRGB = list(pil_img.getdata())
input_size = pil_img.size
rawRGB = np.float32(rawRGB)
end_ts = time.time()
print(end_ts - start_ts)


# convert image to rgba
pil_img = pil_img.convert("RGBA")
end_ts = time.time()
print(end_ts - start_ts)


# flatten 3 dimensional RGB data to one dimension with a black and white approximation of the image
result = np.float32(np.dot(rawRGB, [[0.21], [0.72], [0.07]]))
end_ts = time.time()
print(end_ts - start_ts)


# classify each pixel as either text or background
threshold = 150
#labels = list(map(lambda x:x<threshold, result))
labels = result.clip(min=threshold) - threshold
end_ts = time.time()
print(end_ts - start_ts)


# reassign pixel values based on classification labels
newData = []
for i in labels:
	if i:
		newData.append((255, 255, 255, 0))
	else:
		newData.append((0, 0, 0, 255))

# built output image
output_img = Image.new("RGBA", (input_size[0], input_size[1]))
output_img.putdata(newData)
output_img.save("output.png", "PNG")

end_ts = time.time()
print(end_ts - start_ts)
print("---------------------------------------------------------")
