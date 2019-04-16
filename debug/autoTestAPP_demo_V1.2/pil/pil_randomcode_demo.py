from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

# 打开一个jpg图像文件:
im = Image.open('./image/mao.jpg')
# 获得图像尺寸:
w, h = im.size

# 缩放到50%:
#im.thumbnail((w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('./image/mao2.jpg', 'jpeg');
#im.save('./image/mao2.jpg')

#生成图片验证码
# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))

# 创建Font对象:
#font = ImageFont.truetype('Arial.ttf', 36)
font =ImageFont.truetype('C:/windows/fonts/Arial.ttf', 36)

# 创建Draw对象:
draw = ImageDraw.Draw(image)

# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())

# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())

# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('./image/code.jpg', 'jpeg')
image.show()
