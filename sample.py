#generate text files
import os
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import cv2
import pytesseract
import unicodedata

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
path = 'Main_Code/txt_files'


def text_2_png(text, full_path, color="#000", bgcolor="#FFF", fontfullpath=None, fontsize=15, leftpadding=3,
               rightpadding=3, width=500):

    replacement_character = u'\uFFFD'
    newline_replacement_string = ' ' + replacement_character + ' '

    # prepare linkback
    linkback = "created via http://ourdomain.com"
    fontlinkback = ImageFont.truetype('font.ttf', 10)
    linkbackx = fontlinkback.getsize(linkback)[0]
    linkback_height = fontlinkback.getsize(linkback)[1]
    # end of linkback

    font = ImageFont.load_default() if fontfullpath is None else ImageFont.truetype(fontfullpath, fontsize)
    text = text.replace('\n', newline_replacement_string)

    lines = []
    line = u""

    for word in text.split():
        print(word)
        if word == replacement_character:  # give a blank line
            lines.append(line[1:])  # slice the white space in the begining of the line
            line = u""
            lines.append(u"")  # the blank line
        elif font.getsize(line + ' ' + word)[0] <= (width - rightpadding - leftpadding):
            line += ' ' + word
        else:  # start a new line
            lines.append(line[1:])  # slice the white space in the begining of the line
            line = u""

            # TODO: handle too long words at this point
            line += ' ' + word  # for now, assume no word alone can exceed the line width

    if len(line) != 0:
        lines.append(line[1:])  # add the last line

    line_height = font.getsize(text)[1]
    img_height = line_height * (len(lines) + 1)

    img = Image.new("RGBA", (width, img_height), bgcolor)
    draw = ImageDraw.Draw(img)

    y = 0
    for line in lines:
        draw.text((leftpadding, y), line, color, font=font)
        y += line_height

    # add linkback at the bottom
    draw.text((width - linkbackx, img_height - linkback_height), linkback, color, font=fontlinkback)

    img.save(full_path)


def read_text_files(file_path):
    with open(file_path, encoding='utf8') as f:
        s = f.read()
        generated_img_path = f'../imgs/{(file_path.split("."))[0]}.png'
        text_2_png(s, generated_img_path, fontfullpath="font.ttf")


def img_2_text(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    y = pytesseract.image_to_string(img)
    x = unicodedata.normalize('NFKD', y).encode('ascii', 'ignore')
    x = x.decode("utf-8")
    f = open(f'../final_txt_files/{image_path.split(".")[0]}.txt', 'w')
    f.write(x)
    f.close()


os.chdir(path)

for file in os.listdir():
    if file.endswith('.txt'):
        read_text_files(f'{file}')

os.chdir('../imgs')

for file in os.listdir():
    if file.endswith('.png'):
        img_2_text(f'{file}')
