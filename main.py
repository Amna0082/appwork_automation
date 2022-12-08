import time

import driver as driver

from _cffi_backend import string
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

# driver: WebDriver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

 # chromedriver_path = r'/usr/local/bin/chromedriver'
driver = webdriver.Chrome()

driver.get("https://admin.appworkco-beta.com/sessions")
driver.find_element(By.ID, 'create_email').send_keys('dastor@dasmenresidential.com')
driver.find_element(By.ID, 'create_password').send_keys('M4sterchi3f')
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/form/div[4]/button').click()
print(driver.title)
el = driver.find_element(By.XPATH, '//*[@id="sidebar-app"]/div/div[4]/div/div[1]/div[1]/div')
print(el.click())
from selenium.common.exceptions import WebDriverException

try:
    el.click()
    print("element clicked")
    el2 = driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/div/div[4]/div/div[2]/div/div/div[1]/div[1]/a')
    el2.click()

except WebDriverException:
    print("Element is not clickable")

try:
    print("logout--->", driver.find_element(By.XPATH,
                                            '//*[@id="sidebar-app"]/div/div[4]/div/div[2]/div/div/div[1]/div[2]/div[2]').click())
except WebDriverException:
    print("logoed error")


driver.get("https://admin.appworkco-beta.com/sessions")

driver.find_element(By.ID, 'create_email').send_keys('dastor@dasmenresidential.com')
driver.find_element(By.ID, 'create_password').send_keys('M4sterchi3f')
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/form/div[4]/button').click()
print(driver.title)
driver.find_element(By.XPATH, '//*[@id="sidebar-app"]/div/div[4]/div/div[1]/div[1]/div').click()
driver.implicitly_wait(1000)
driver.find_element(By.XPATH, '//*[@id="system-settings-app"]/div/div/a[1]/div').click()
# driver.implicitly_wait(1000)
#el3 = driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div[4]/div[2]/div[1]/div[1]/div/input').send_keys('https://www.google.com/')
try:
    print("element clicked el3")
    el3 = driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div[4]/div[2]/div[1]/div[1]/div/input')
    driver.execute_script("arguments[0].value = 'https://www.google.com/'", el3)
    #el3.send_keys('https://www.google.com/')
    print("Value of input box: " + el3.get_attribute('value'))
    print('click logo url el3')

except WebDriverException:
    print("Element click ni hu raa el3")

try:
    print("element clicked el4")
    el4 = driver.find_element(By.XPATH, '//*[@id="rc-editable-input-1"]')
    driver.execute_script("arguments[0].value = ''", el4)
    el4.clear()
    el4.send_keys('#DB0B0B')
    print("Value of input box: " + el4.get_attribute('value'))
    #set_value_xpath(driver, '//*[@id="rc-editable-input-1"]', '#EA7607')
    print('Select value from color picker el4')

except WebDriverException:
    print("Choose value from input color ")

try:
    print("element clicked el5")
    el5 = driver.find_element(By.XPATH, '//*[@id="rc-editable-input-2"]')
    driver.execute_script("arguments[0].value = ''", el5)  #get attribute and then it will clear the already given value then will set new one
    el5.clear()
    el5.send_keys('#E6780C')
    print("Value of input box: " + el5.get_attribute('value'))
    print('Select value from color picker el5')

except WebDriverException:
    print("Choose value from input color el5")

try:
    print("element clicked el6")
    el6 = driver.find_element(By.XPATH, '//*[@id="rc-editable-input-3"]')
    driver.execute_script("arguments[0].value = ''", el6)
    el6.clear()
    print("Value of input box before send keys: " + el6.get_attribute('value'))
    el6.send_keys('#0F13D8')
    print("Value of input box: " + el6.get_attribute('value'))
    print('Select value from color picker el6')

except WebDriverException:
    print("Choose value from input color el6 ")

try:
    print("element clicked el7")
    el7 = driver.find_element(By.XPATH, '//*[@id="rc-editable-input-4"]')
    driver.execute_script("arguments[0].value = ''", el7)
    el7.clear()
    el7.send_keys('#AE1F89')
    print("Value of input box " + el7.get_attribute('value'))
    print('Select value from color picker el7')

except WebDriverException:
    print("Choose value from input color el7 ")
driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div[4]/div[2]/div[2]/button').click()
time.sleep(10000)
driver.refresh()
#Logo Url reset button
driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div[4]/div[2]/div[1]/div[1]/a').click()
driver.switchTo().alert().dismiss()
driver.switchTo().alert().accept()
driver.switchTo().alert().getText()

# driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div[4]/div[2]/div[1]/div[2]/a').click()
#
# driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div[4]/div[2]/div[1]/div[3]/a').click()
#
# driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div[4]/div[2]/div[1]/div[4]/a').click()
#
# driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div[4]/div[2]/div[1]/div[5]/a').click()

driver.refresh()

# assert "No results found." not in driver.page_source
# actualUrl ="https://admin.appworkco-beta.com/sessions";
# expectedUrl = driver.current_url
# assert actualUrl == expectedUrl