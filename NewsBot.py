from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests

import sys

# Define your API information

browser = webdriver.Firefox()#firefox_options=options)
url = "https://news.google.com/?hl=en-IN&gl=IN&ceid=IN:en"
root = "https://news.google.com"
browser.get('https://web.whatsapp.com')
print('Scan and get started')
sleep(20)
while True:
	unread = browser.find_elements_by_class_name("OUeyt")
	if len(unread) > 0:
		ele = unread[0]
		action = webdriver.common.action_chains.ActionChains(browser)
		action.move_to_element_with_offset(ele, 0, -20)
		action.click()
		action.perform()
		try:
			action.click()
			action.perform()
		except:
			continue
		name = browser.find_element_by_class_name("_2zCDG").text
		messages = browser.find_elements_by_class_name("_3zb-j")
		query = messages[-1].text
		if 'news' in query.lower():
			text_box = browser.find_element_by_class_name("_2S1VP")
			response = "Hi "+name+". Aravind's Bot here :). Let me and fetch send top 5 latest news:\n"
			text_box.send_keys(response)
			soup = BeautifulSoup(requests.get(url).content, "html5lib")
			articles = soup.find_all('article', class_="MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d YKEnGe EyNMab t6ttFe Fm1jeb EjqUne")
			news = [i.find_all('a',class_="ipQwMb Q7tWef")[0].text for i in articles[:5]]
			links = [root+i.find('a')['href'][1:] for i in articles[:5]]
			links = [requests.get("http://thelink.la/api-shorten.php?url="+link).content.decode() for link in links]
			for i in range(5):
				text_box.send_keys(news[i] + "==>" + links[i] + "\n")
		sleep(1)
	sleep(1)