import time

import driver as driver

from _cffi_backend import string
from pip._internal.models import link
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

#driver: WebDriver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
 # chromedriver_path = r'/usr/local/bin/chromedriver'
driver = webdriver.Chrome()

driver.get("https://www.wikipedia.org/")
# to select dropdown values
dropdown = driver.find_element(By.ID, 'searchLanguage')
select = Select(dropdown)
#select.select_by_visible_text("Eesti")
select.select_by_value("hi")

options = driver.find_element(By.TAG_NAME, 'option')
for option in options:
    print('Text is :', option.text, 'lang is :', +option.get_attribute('lang'))

print('total dropdown values are', len(options))

# To select all link on the page/website

links = driver.find_element(By.TAG_NAME, 'a')
print(len(links))
for Link in links:
    print('Test is :', link.text, ' --URL is:', +link.get_attribute('href'))

# To select all link with in the block
# block = driver.find_element(By.XPATH, '')
#
# Links = block.find_element(By.TAG_NAME, 'a')
# print(len(Links))
# for Link in Links:
#     print('Test is : ', Link.text ', --URL is:' + Link.get_attribute('herf'))
