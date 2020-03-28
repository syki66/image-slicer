from PIL import Image

img = Image.open('suvin.png')

pic_size = img.size[1]

last_pic = pic_size % 3000

i = 0

while(pic_size / 3000 >i+1):
    box = (0,(3000*i)+i,758,(3000*i)+i+3000)
    img2 = img.crop(box)
    img2.save('상세페이지 수정본'+str(i+1)+'.png')
    i+=1

box = (0,(3000*i)+i,758,(3000*i)+i+last_pic)
img2 = img.crop(box)
img2.save('상세페이지 수정본'+str(i+1)+'.png')
