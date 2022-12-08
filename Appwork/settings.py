import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException

driver = webdriver.Chrome()
driver.get("https://admin.appworkco-beta.com/sessions")
driver.find_element(By.ID, 'create_email').send_keys('1talha@invozone.com')
driver.find_element(By.ID, 'create_password').send_keys('1p@ssw0rd#!')
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/form/div[4]/button').click()

# error_message = "Invalid Login"
# # get the errors (if there are)
# errors = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]')
# time.sleep(1)
# # email field
# driver.find_element(By.ID, 'create_email').send_keys('dastor@dasmenresidential.com')
# # password field
# driver.find_element(By.ID, 'create_password').send_keys('M4sterchi3f')
# # click on login button
# driver.find_element(By.XPATH, '/html/body/div[1]/div/div/form/div[4]/button').click()

# driver.find_element(By.XPATH, '//*[@id="sidebar-app"]/div/div[4]/div/div[1]/div[1]/div').click()
# time.sleep(2)

# driver.find_element(By.XPATH, '//*[@id="sidebar-app"]/div/div[4]/div/div[2]/div/div/div[1]/div[2]/div[2]').click()
# time.sleep(2)
# # email field
# driver.find_element(By.ID, 'create_email').send_keys('dastor@dasmenresidential.com')
# # password field
# driver.find_element(By.ID, 'create_password').send_keys('M4sterchi3f')
# # click on login button
# driver.find_element(By.XPATH, '/html/body/div[1]/div/div/form/div[4]/button').click()
# sidebar popup
driver.find_element(By.XPATH, '//*[@id="sidebar-app"]/div/div[4]/div/div/div[1]/div').click()
time.sleep(3)
# settings button
driver.find_element(By.XPATH, '//*[@id="sidebar-app"]/div/div[4]/div/div[2]/div/div/div[1]/div[1]/a').click()
driver.implicitly_wait(100)
# application settings
driver.find_element(By.XPATH, '//*[@id="system-settings-app"]/div/div/a[1]/div').click()
# # setting logo url
# driver.implicitly_wait(100)
# driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div/div[3]/div[1]/div').click()
# print("element clicked el3")
# time.sleep(2)
# try:
#     el3 = driver.find_element(By.XPATH, '/html/body/div[4]/main/div/div/div/div/div[4]/div[2]/div[1]/div[1]/div/input')
#     driver.execute_script("arguments[0].value = ''", el3)
#     el3.send_keys('https://www.google.com/')
#     print("Value of input box: " + el3.get_attribute('value'))
# except WebDriverException:
#     print("errorrrrrrr--------->>>>>>")
# time.sleep(1)
#
# try:
#     print("element clicked el4")
#     el4 = driver.find_element(By.XPATH, '//*[@id="rc-editable-input-1"]')
#     driver.execute_script("arguments[0].value = ''", el4)
#     # el4.clear()
#     el4.send_keys('#DB0B0B')
#     print("Value of input box: " + el4.get_attribute('value'))
#     #set_value_xpath(driver, '//*[@id="rc-editable-input-1"]', '#EA7607')
#     print('Select value from color picker el4')
#
# except WebDriverException:
#     print("Choose value from input color ")
# time.sleep(1)
#
# try:
#     print("element clicked el5")
#     el5 = driver.find_element(By.XPATH, '//*[@id="rc-editable-input-2"]')
#     driver.execute_script("arguments[0].value = ''", el5)  #get attribute and then it will clear the already given value then will set new one
#     # el5.clear()
#     el5.send_keys('#E6780C')
#     print("Value of input box: " + el5.get_attribute('value'))
#     print('Select value from color picker el5')
#
# except WebDriverException:
#     print("Choose value from input color el5")
# time.sleep(1)
#
# try:
#     print("element clicked el6")
#     el6 = driver.find_element(By.XPATH, '//*[@id="rc-editable-input-3"]')
#     driver.execute_script("arguments[0].value = ''", el6)
#     # el6.clear()
#     print("Value of input box before send keys: " + el6.get_attribute('value'))
#     el6.send_keys('#0F13D8')
#     print("Value of input box: " + el6.get_attribute('value'))
#     print('Select value from color picker el6')
#
# except WebDriverException:
#     print("Choose value from input color el6 ")
# time.sleep(1)
#
# try:
#     print("element clicked el7")
#     el7 = driver.find_element(By.XPATH, '//*[@id="rc-editable-input-4"]')
#     driver.execute_script("arguments[0].value = ''", el7)
#     # el7.clear()
#     el7.send_keys('#AE1F89')
#     print("Value of input box " + el7.get_attribute('value'))
#     print('Select value from color picker el7')
#
# except WebDriverException:
#     print("Choose value from input color el7 ")
#
# # To Save theme Setting page
# time.sleep(2)
# driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/button').click()
# time.sleep(2)
# # To Show alert and click on Ok from alert popup
# alert = driver.switch_to.alert
# alert.accept()
# #Logo Url reset button
# time.sleep(1)
# driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[1]/div[1]/a').click()
# time.sleep(1)
# alert = driver.switch_to.alert
# alert.accept()
# # Reset Primary Color
# time.sleep(1)
# driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[1]/div[2]/a').click()
# time.sleep(1)
# alert = driver.switch_to.alert
# alert.accept()
# # Reset Secondary Color
# time.sleep(2)
# driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[1]/div[3]/a').click()
# time.sleep(2)
# alert = driver.switch_to.alert
# alert.accept()
# # Reset Sidebar Color
# time.sleep(2)
# driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[1]/div[4]/a').click()
# time.sleep(2)
# alert = driver.switch_to.alert
# alert.accept()
# # Reset Sidebar Text Color
# time.sleep(2)
# driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[1]/div[5]/a').click()
# time.sleep(2)
# alert = driver.switch_to.alert
# alert.accept()
# driver.refresh()
# time.sleep(2)

#Click on Property settings
driver.refresh()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div/div[1]/div/div[2]/div').click()
#Click on General tab
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div/div[3]/div[1]/div').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div/div[2]/div[1]/div/div').click()  #Selct property from Property Selector
driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div/div[2]/div[1]/div[2]/div[1]/input').send_keys('johar town')  # property selector search
driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div').click()
driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div/div[2]/div[2]/button').click()  #Deactivate Property button
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div/div[2]/div[2]/button').click()  #activate property
time.sleep(3)
elm = driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[2]/input')
elm.clear()
elm.send_keys('johar Town')
driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/div[2]/div[2]/input').send_keys('284 j block ')  #Property Address
driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/div[3]/input[1]').send_keys('Lahore')  #City
driver.execute_script("document.getElementsByClassName('css-1uccc91-singleValue')[0].innerHTML = 'Kansas'")
driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/div[3]/input[2]').click().send_keys('54000')
driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/div[4]/div/div[2]/input').click().send_keys('123456789')  #phon
driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/div[5]/div/div[2]/input').clear().send_keys('https://www.google.com/')
driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/div[6]/div/div[2]/input').click().send_keys('test@test.com')    #email
driver.execute_script("document.getElementsByClassName(' css-1uccc91-singleValue')[1].innerHTML = 'US/Mountain '")  #Time Zone
driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/div[9]/div/div[2]').send_keys('1005')   #Integration ID
driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[1]/div[2]/div/label/i').send_keys('/Users/amnakhalid/Downloads/logo.webp') #upload Logo
driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[1]/div[4]/div/label/i').send_keys('/Users/amnakhalid/Downloads/download icon.png')  #upload icon
driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[1]/div[4]/div/label/i').send_keys('/Users/amnakhalid/Downloads/Banner.jpeg')  #upload Banner

driver.refresh()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div/div[3]/div[2]/div').click()  #Application Tab
driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div/div[3]/div[2]/div').click()  #Application
driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[1]/div[1]/div/div[2]').click() #Accepting Applications
driver.find_element(By.XPATH, '').clear().send_keys()



# time.sleep(5)
# driver.close()
