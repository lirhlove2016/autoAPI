from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

#-------------------------------------
'''
image= Image.open('./image/name.jpg')
draw=ImageDraw.Draw(image)

#搜索
x1,y1=[837,103]
x2,y2=[942,208]

draw.line([x1,y2,x2,y2],fill ="red",width=5)   #线
#draw.rectangle((x1, y1, x2,y2), fill='black', outline ='red',width=5)  #矩形 fill填充，outline外线
#draw.rectangle((x1, y1, x2,y2), outline ='red',width=5)  #矩形
draw.arc((x1, y1, x2,y2), 0, 180, 'blue',width=5)   #半圆
#draw.ellipse((x1, y1, x2,y2), 'green', 'wheat',width=5)   #椭圆
draw.ellipse((x1, y1, x2,y2), outline= 'green',width=5)
#draw.polygon([(x1,y1),(x2,y1),(x2,y2),(x1,y2)], outline=(255,0,0))

#sign
x1,y1=[744,276]
x2,y2=[1014,366]
draw.rectangle((x1,y1,x2,y2),outline = "red",width=5)  #outline 外线，fill填充

font = ImageFont.truetype("consola.ttf", 40, encoding="unic")#设置字
draw.text((100, 50), 'Hello World', 'fuchsia', font)
image.show()
'''

#图片处理，框选
def pic_rectangle(filepath,bound):
    image = Image.open(filepath)
    draw = ImageDraw.Draw(image)
    # 坐标
    x1, y1 =bound[0]
    x2, y2 =bound[1]
    # outline 外线，fill填充
    draw.rectangle((x1, y1, x2, y2), outline="red", width=5)
    image.save('filepath', 'jpeg')
    #image.show()

if  __name__=="__main__":
    #调用
    filepath="./image/name.jpg"
    bound=[[744, 276],[1014, 366]]
    pic_rectangle(filepath,bound)
