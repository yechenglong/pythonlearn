from PIL import Image
from urllib import request
# 定义要转换的字符串
char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
# 定义字符图的长宽
WIDTH = 90
HEIGHT = 45
# 定义下载图片的地址和保存地址
img_path = "test.png"
img_url = "http://labfile.oss.aliyuncs.com/courses/370/test.png"
# 定义灰度值转换字符函数
def gray2char(r,g,b,alpha=256):
    if alpha == 0 :
        return  ' '
    gray = int(0.299 * r + 0.578 * g + 0.114 * b)#计算灰度值
    length = len(char)
    #映射灰度值对应的字符
    unit = 256/length
    return char[int(gray/unit)]

if __name__ == "__main__":
    #下载图片
    request.urlretrieve(img_url,img_path)
    im = Image.open(img_path)
    im = im.resize((WIDTH,HEIGHT),Image.NEAREST)
    txt = ''
    # for i in range(HEIGHT):
    #     for j in range(WIGHT):
    #         txt += gray2char(*im.getpixel((j,i)))
    #     txt += '\n'
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += gray2char(*im.getpixel((j,i)))
        txt += '\n'
    print(txt)
    with open("output.txt","w") as f:
        f.write(txt)


