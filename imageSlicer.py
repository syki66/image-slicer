from PIL import Image

fileName = "suvin.png"

img = Image.open(fileName)

# 위메프는 세로길이 3000px, 옥션은 2580px
cropped_height = 2580

pic_width, pic_height = img.size

print(pic_width)

last_pic = pic_height % cropped_height

i = 0

while(pic_height / cropped_height >i+1):
    box = (0,(cropped_height*i)+i,pic_width,(cropped_height*i)+i+cropped_height)
    img2 = img.crop(box)
    img2.save(fileName.split(".")[0]+str(i+1)+'.'+ fileName.split(".")[1])
    i+=1

box = (0,(cropped_height*i)+i,pic_width,(cropped_height*i)+i+last_pic)
img2 = img.crop(box)
img2.save(fileName.split(".")[0]+str(i+1)+'.'+fileName.split(".")[1])
