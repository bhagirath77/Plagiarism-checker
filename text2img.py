import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import unicodedata
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def text2png(text, fullpath, color="#000", bgcolor="#FFF", fontfullpath=None, fontsize=13, leftpadding=3,
             rightpadding=3, width=200):
    REPLACEMENT_CHARACTER = u'\uFFFD'
    NEWLINE_REPLACEMENT_STRING = ' ' + REPLACEMENT_CHARACTER + ' '

    font = ImageFont.load_default() if fontfullpath == None else ImageFont.truetype(fontfullpath, fontsize)
    text = text.replace('\n', NEWLINE_REPLACEMENT_STRING)

    lines = []
    line = ""

    for word in text.split(" "):
        if word == REPLACEMENT_CHARACTER:  # give a blank line
            lines.append(line[1:])  # slice the white space in the begining of the line
            line = ""
            lines.append("")  # the blank line
        elif font.getsize(line + ' ' + word)[0] <= (width - rightpadding - leftpadding):
            line += ' ' + word
        else:  # start a new line
            lines.append(line[1:])
            # slice the white space in the begining of the line
            line = ""

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

    img.save(fullpath)

# show time
f = open("ex.txt", encoding="utf8")
x = f.read()
text2png(x, 'test.png', fontfullpath="verdanab.ttf")
img = cv2.imread('test.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
y = pytesseract.image_to_string(img)
x = unicodedata.normalize('NFKD', y).encode('ascii', 'ignore')
x = x.decode("utf-8")
print(x)