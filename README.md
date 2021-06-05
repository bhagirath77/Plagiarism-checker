Plagiarism checker

The aim of the project is to create a plagiarism checker for text files.

The main focus is going to be on countering the problem of obfuscated text being used by the students to tackle plagiarism check.

First of all, import the necessary packages,

Give the path for pytesseract according to how you have placed it in your desktop
```python
import os
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import unicodedata
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
```

First of all, we need to read all the files. To counter the problem of obfuscated text, we will be converting all the text files into images.

While converting them to images, we will convert the Diacritics that have been used by the students to in the aplhabets to their root form. 
An example of a Diacritic for e is é,è,ê,ë,ē . 

```python
path = 'txt_files'
os.chdir(path)

for file in os.listdir():
    if file.endswith('.txt'):
        read_text_files(f'{file}')

os.chdir('../imgs')

def read_text_files(file_path):
    with open(file_path, encoding='utf8') as f:
        s = f.read()
        generated_img_path = f'../imgs/{(file_path.split("."))[0]}.png'
        text2png(s, generated_img_path, fontfullpath="font.ttf")

```

Another tactic that students can use is using symbols similar to the english alphabets that are of different origin. For example, the character alpha i.e. α looks similar to a or the character rho i.e. ρ looks like p.

One of the limitations of pytesseract is that it reads symbols similar to the enlgish alphabets as the alphabets themselves.
So, using openCV and pytesseract ,we read the images and create new text files with the same initial name. 

```python
for file in os.listdir():
    if file.endswith('.png'):
        img_2_text(f'{file}')
```

Now that we have converted the obfuscated text to root form, we start checking for plagiarism between each pair of files.
We have used rolling hash, tokenization and winnowing dynamically to write the code for checking plagiarism. 

The data of plagiarism is being stored in a dictionary which is printed in the end. 
