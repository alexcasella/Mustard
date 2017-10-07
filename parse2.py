from PIL import Image

img = Image.open('/Users/alex/Desktop/Projects/Mustard/Images/img2.png')
img = img.convert("RGBA")
datas = img.getpixel((0, 0))

print(datas)

# newData = []
# for item in datas:
#     if item[0] == 255 and item[1] == 255 and item[2] == 255:
#         newData.append((255, 255, 255, 0))
#     else:
#         newData.append(item)

# img.putdata(newData)
# img.save("img2.png", "PNG")
