from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import pyautogui
from loreal import caption
import os

options = Options()
options.set_headless(headless=True)
browser = webdriver.Firefox()#firefox_options=options)
url = "https://news.google.com/?hl=en-IN&gl=IN&ceid=IN:en"
root = "https://news.google.com"
browser.get('https://web.whatsapp.com')
print('Scan and get started')
sleep(10)

path = '/Users/Karan/Downloads/WhatsappTest.jpg' #Your Downloads Path Here (Keep WhatsappTest.jpg as it is)

def save(image):
	action.context_click(image).perform()
	pyautogui.typewrite(['down','down','down','down','enter'])
	file = ' WhatsappTest'
	pyautogui.typewrite(file)
	sleep(0.5)
	pyautogui.typewrite(['enter'])

while True:
	unread = browser.find_elements_by_class_name("OUeyt")
	if len(unread) > 0:
		ele = unread[-1]
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
		messages = browser.find_elements_by_class_name("vW7d1")
		images = messages[-1].find_elements_by_class_name("_3v3PK")
		if len(images) != 0:
			image = images[-1]
			text_box = browser.find_element_by_class_name("_2S1VP")
			response = "Hi "+name+". Aravind's bot here. Let me analyze the image and say what it is\n"
			text_box.send_keys(response)
			action = webdriver.common.action_chains.ActionChains(browser)
			print('New image found, saving')
			sleep(5)
			save(image)
			try:
				cap = caption(path)
			except:
				cap = "sorry i dont understand this image"
			text_box.send_keys('Prediction : "'+cap.capitalize()+'"\n')
			os.remove(path) # Cleanup
	sleep(2)