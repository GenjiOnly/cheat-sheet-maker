# -*-coding:utf-8-*-

from PIL import Image, ImageFont, ImageDraw
import chardet
import re


# 读取文本中的内容，并返回一个字典，命令和解释一一对应
def get_content():
    words = dict()
    keys = list()
    values = list()
    with open('dic.txt') as fp:
        for line in fp.readlines():
            if len(line) <= 5 :
                pass
            else :
                line = line.strip('\n').decode('utf-8')
                match = re.compile('\s')
                keys.append(match.split(line)[0])
                values.append(match.split(line)[1])
                words = dict(dict(zip(keys, values)).items() + words.items())
        fp.close()
    # print words
    return words


def draw(width, height, words):
    # 背景色
    bgcolor = '#000000'

    image = Image.new('RGB', (width, height), bgcolor)

    # 加载字体
    path = 'C:/windows/fonts/Arial.ttf'
    path.decode('utf-8').encode('utf-8')
    font = ImageFont.truetype(path, 13)

    font2 = ImageFont.truetype('msyh.ttf', 13)

    draw = ImageDraw.Draw(image)

    n = 0
    wid = 170
    for word in words:
        n += 1
        width = wid
        height = 30 * n + 100
        draw.text((width, 10 + height), word, font=font, fill='#DCD5C9')
        draw.text((width + 130, 10 + height),
                  words[word], font=font2, fill='#DCD5C9')

        if height > 800 :
            wid = width + 600
            n = 0.5

    #image.show()
    image.save('1.jpg','jpeg')

if __name__ == '__main__':
    draw(1920, 1080, get_content())
