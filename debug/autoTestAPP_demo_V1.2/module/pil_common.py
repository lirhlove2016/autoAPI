from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

#-------------------------------------
#filepath,[837,103][942,208]
#图片处理，框选
def pic_rectangle(filepath,bound):
    print('正在处理图片-------------')
    #print(filepath,bound)
    image = Image.open(filepath)
    draw = ImageDraw.Draw(image)
    # 坐标
    x1, y1 =bound[0]
    x2, y2 =bound[1]

    print('---------------',x1, y1, x2, y2)
    # outline 外线，fill填充
    draw.rectangle((x1, y1, x2, y2), outline="red", width=5)
    image.save('filepath', 'jpeg')
    image.show()

if  __name__=="__main__":
    #调用
    filepath="./image/name.jpg"
    bound=[[744, 276],[1014, 366]]
    pic_rectangle(filepath,bound)
