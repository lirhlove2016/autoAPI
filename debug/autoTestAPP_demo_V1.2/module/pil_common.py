from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

#-------------------------------------
#filepath,[837,103][942,208]
#图片处理，框选
def pic_rectangle2(filepath,bound):
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
    image.save(filepath, 'jpeg')
    image.show()

#图片处理，框选
def pic_rectangle(filepath,bound):
    print('正在处理图片-------------')
    #print(filepath,bound)
    image = Image.open(filepath)
    draw = ImageDraw.Draw(image)
    # 坐标
    x1 = bound[0]
    y1 = bound[1]
    x2 = bound[2]
    y2 = bound[3]

    print('---------------',x1, y1, x2, y2)
    # outline 外线，fill填充
    draw.rectangle((x1, y1, x2, y2), outline="red", width=5)
    image.save(filepath, 'jpeg')
    print('图片保存')
    #image.show()

#提取坐标
def  get_bounds_xy(bouds):
    #[488,308][668,368]
    xx,yy=bouds.split('][')
    print(xx,yy)
    x1,y1=xx.split(",")
    x1=x1.split('[')[1]
    x2,y2=yy.split(",")
    y2 = y2.split(']')[0]
    print('提取坐标x1, y1, x2, y2---------------', int(x1), int(y1), int(x2), int(y2))
    return int(x1), int(y1), int(x2), int(y2)

if  __name__=="__main__":
    # 调用
    filepath = "./report/image/shujia_2.jpg"
    bound = [[488,308],[668,368]]
    image.pic_rectangle2(filepath, bound)

    #获取坐标
    recxy=get_bounds_xy(t)
    print(recxy,recxy[0])
    #调用图片处理
    filepath = "./report/image/shujia_1.png"
    image.pic_rectangle(filepath, recxy)
