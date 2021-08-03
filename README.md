# Plagiarism Checker for documents

### Aim 
The main aim of our plagiarism checker is to counter the problem of the usage of diacritics and symbols that look like the English 
alphabetical characters. An example of such a case is : the similarity in the character a and α (symbol of alpha).
There are many more similar symbols such as β,γ or ρ. Examples of diacritics are á, à , â , ü or ñ.

### Requirements:

First of all , you will have to install the following libraries before running the code by using the following commands.


```python
pip install python-csv
pip install unicodedata ( #if not found do : pip install unicodedata2 )
pip install pytesseract
pip install opencv-python
pip install tk
```

First, a GUI application will open in which you have to select the directories containing the required text documents.

We have added an additional feature where you can also select individual text documents that you want to add in case there is a high probability of the users using the text resource for the assignment.

Now you just have to click on the 'Start code' button and you will get an excel sheet as a final result containing pairs of names of the students and the respective plagiarism percentage. 

### Working

First of all , we will convert our text into image and then we will convert it back into text dicument. 


We are going to use tesseract OCR to convert image into text. This way, it will read all the sybmols as alphabets.
For exmaple, it will read the character alpha α as a and similarly for all other symbols.`


Next we will convert the diacritics to their root form. To do this, we have written the code given below:
(Here x is the string that we got using the tesseract OCR)
```python
x = unicodedata.normalize('NFKD', y).encode('ascii', 'ignore')
x = x.decode("utf-8")
```

After this, we will have our finally text files after the preprocessing.

Now we will find the plagiarism percentage for any pair of files and if the percentage is higher than the threshold, they will be added to the table containing
 list of plagiarised documents. 

For finding out plagiarism , we have used hashing , tokenization and winnowing. 

