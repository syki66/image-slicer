from PIL import Image

fileName = "suvin.png"

img = Image.open(fileName)

pic_width, pic_height = img.size

print(pic_width)

last_pic = pic_height % 3000

i = 0

while(pic_height / 3000 >i+1):
    box = (0,(3000*i)+i,pic_width,(3000*i)+i+3000)
    img2 = img.crop(box)
    img2.save(fileName.split(".")[0]+str(i+1)+'.'+ fileName.split(".")[1])
    i+=1

box = (0,(3000*i)+i,pic_width,(3000*i)+i+last_pic)
img2 = img.crop(box)
img2.save(fileName.split(".")[0]+str(i+1)+'.'+fileName.split(".")[1])
