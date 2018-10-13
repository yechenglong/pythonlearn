from PIL import Image
import requests
ascii_char = list("1234567890-=!@#$%^&*()_+qwertyuiop[]asdfghjkl;'zxcvbnm,./{}|:<>?\" ")
url = "http://labfile.oss.aliyuncs.com/courses/370/test.png"#"http://labfile.oss.aliyuncs.com/courses/370/ascii_dora.png"
WIDTH = 90
HEIGHT = 45
def image2char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    length = len(ascii_char)
    return ascii_char[int(gray/(256/length))]

if __name__ =='__main__':
    ir=requests.get(url)
    with open("13.png", 'wb') as f:
        f.write(ir.content)

    im = Image.open('13.png')
    im = im.resize((WIDTH,HEIGHT),Image.NEAREST)
    txt = ''
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += image2char(*im.getpixel((j,i)))
        txt += '\n'
    print(txt)
    with open("output.txt", 'w') as f:
        f.write(txt)




