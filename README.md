# Python-Whatsapp-Chatbot
A chatbot built in python using Selenium module. Add your Microsoft Azure API key in loreal.py to run the Image Captioning bot.

## Running the bot
1. Make sure you have put the Azure API key in loreal.py to use the image captioning bot feature.
2. Run the command <code>python3 bot.py</code>
3. Scan the QR code with your phone to start whatsapp web on browser that pops up. (You may have to configure selenium geckodriver depending on the OS you are using. Specify geckodriver.exe's path in selenium inside bot.py file)
4. Ask your friend to send <b>activate bot</b> to you.
5. Now he can either send <b>show news</b> or send an image to start the image Captionig.

Feel free to improve the code and add features.


Currently the chatbot is only capable of the following tasks:

## 1. News show
Run News.py to start the bot with the news mode ON. Any message you will get after you run the bot having the word "news" in it will be treated as a request for latest headlines. The bot then fetches the latest news. 

## 2. Image Captioning Bot
A bot that captions the image sent to you using Microsoft's Azure platform. You will need an API key from Azure to run this. If you dont have one, you can make your own "caption" function and play around the image.
