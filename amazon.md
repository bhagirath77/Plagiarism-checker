# A python App that can track Amazon product prices
The purpose of this app is to track the price of a specific product on a day to day basis and notify you when it falls. In simple words, it is tracking when the sales of a particular product are on the amazon app.

###Pre-requisites 
You will have to download Visual Studio Code or Pycharm to run this app. There are other IDE's but these two are the most user-friendly and it will be more easier to download libraries using it.

First you need to download the following libraries by typing this command in the respective terminals of the IDE:

```python
pip install times
pip install requests bs4 
pip install secure-smtplib
```
If you are using PyCharm, you need to hold you arrow on the import functions for all these libraries and PyCharm will give you the option to install it automatically.

### Product and Credentials

You need to enter your Email address and password in the variables with the respective names . Other than that, you need to copy the URL of the product and past it in 'URL' variable.


After that, you need to click [this](https://www.google.com/search?q=my+user+agent&oq=my+user+age&aqs=chrome.1.69i57j0i433j0l6.2668j1j7&sourceid=chrome&ie=UTF-8) link and copy the first text that shows up and paste it as the value to the key 'User-Agent' .

With this, you are all set to run the code.The code will check the price of the respective product after every 24 hrs and if the price reduces, it wont be checking for the next 7 days. You can either use a VM or your own desktop to run this code.

