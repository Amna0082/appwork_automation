import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Appwork.Locators.locators import Locators

class Utils:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://admin.appworkco-beta.com/sessions")

    def find_element_byid(self,driver,id):
        return driver.find_element(By.ID, id)

    def  find_element_byxpath(self,driver,xpath):
        return driver.find_element(By.XPATH, xpath)

    def find_element_byclassname(self,driver,classname):
        return driver.find_element(By.CLASS_NAME, classname)

    def set_element(self, element, value):
        element.clear()
        return element.send_keys(value)


    def login(self):
        self.set_element(self.find_element_byid(self.driver, 'create_email'), 'dastor1@dasmenresidential.com')
        self.set_element(self.find_element_byid(self.driver, 'create_password'), 'M4sterchi3f1')
        self.find_element_byxpath(self.driver, Locators.login_button).click()
        error_message = "Invalid Login"
        errors = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]')
        time.sleep(2)
        self.set_element(self.find_element_byid(self.driver, 'create_email'), 'dastor@dasmenresidential.com')  # email field
        self.set_element(self.find_element_byid(self.driver, 'create_password'), 'M4sterchi3f')  # password field
        self.find_element_byxpath(self.driver, '/html/body/div[1]/div/div/form/div[4]/button').click()   # click on login button
        # sidebar popup
        self.find_element_byxpath(self.driver, '//*[@id="sidebar-app"]/div/div[4]/div/div/div[1]/div').click()
        time.sleep(3)
        # settings button
        self.find_element_byxpath(self.driver, '//*[@id="sidebar-app"]/div/div[4]/div/div[2]/div/div/div[1]/div[1]/a').click()
        self.driver.implicitly_wait(100)
        # application settings
        self.find_element_byxpath(self.driver, '//*[@id="system-settings-app"]/div/div/a[1]/div').click()
        # setting logo url
        self.driver.implicitly_wait(100)
        self.find_element_byxpath(self.driver, '//*[@id="application-settings-app"]/div/div/div[3]/div[1]/div').click()
        # time.sleep(2)
        self.set_element(self.find_element_byxpath(self.driver, '/html/body/div[4]/main/div/div/div/div/div[4]/div[2]/div[1]/div[1]/div/input'), 'https://www.google.com/') #Application Logo URL
        time.sleep(1)
        self.set_element(self.find_element_byxpath(self.driver, '//*[@id="rc-editable-input-1"]'), '#DB0B0B') #Primary Color
        time.sleep(1)
        self.set_element(self.find_element_byxpath(self.driver, '//*[@id="rc-editable-input-2"]'), '#E6780C') #Secondary Color
        time.sleep(1)
        self.set_element(self.find_element_byxpath(self.driver, '//*[@id="rc-editable-input-3"]'), '#0F13D8') #Sidebar Color
        time.sleep(1)
        self.set_element(self.find_element_byxpath(self.driver, '//*[@id="rc-editable-input-4"]'), '#AE1F89') #Sidebar Text Color
        time.sleep(2)
        self.find_element_byxpath(self.driver, '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/div/button').click()  # To Save theme Setting page)
        time.sleep(2)
        alert = self.driver.switch_to.alert  # To Show alert and click on Ok from alert popup
        alert.accept()
        time.sleep(1)
        self.find_element_byxpath(self.driver, '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[1]/div[1]/a').click()  #Logo Url reset button
        time.sleep(1)
        alert = self.driver.switch_to.alert
        alert.accept()
        time.sleep(1)
        self.find_element_byxpath(self.driver,'//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[1]/div[2]/a').click()   # Reset Primary Color
        time.sleep(1)
        alert = self.driver.switch_to.alert
        alert.accept()
        time.sleep(2)
        self.find_element_byxpath(self.driver, '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[1]/div[3]/a').click() # Reset Secondary Color
        time.sleep(2)
        alert = self.driver.switch_to.alert
        alert.accept()
        time.sleep(2)
        self.find_element_byxpath(self.driver, '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[1]/div[4]/a').click() # Reset Sidebar Color
        time.sleep(2)
        alert = self.driver.switch_to.alert
        alert.accept()
        time.sleep(2)
        self.find_element_byxpath(self.driver, Locators.reset_sidebar).click() # Reset Sidebar Text Color
        time.sleep(2)
        alert = self.driver.switch_to.alert
        alert.accept()
        self.driver.refresh()
        time.sleep(2)

#Maintenance Tab under property settings
        self.driver.refresh()
        time.sleep(3)
        self.find_element_byxpath(self.driver, Locators.maintenance_tab).click()
        time.sleep(2)
# Click on work order block
        self.find_element_byxpath(self.driver, Locators.workorder_block).click()
#Export work orders to integrated system "Switch button turn off"
        self.find_element_byxpath(self.driver, Locators.export_switch_button).click()
        time.sleep(3)
# Export Work Orders save button
        self.find_element_byxpath(self.driver, Locators.save_export).click()
        time.sleep(3)
        alert = self.driver.switch_to.alert
        alert.accept()
#Maintenance Tab under property settings
        self.driver.refresh()
        time.sleep(5)
        self.find_element_byxpath(self.driver, '//*[@id="application-settings-app"]/div/div/div[3]/div[3]/div').click()
        time.sleep(5)
#Export work orders to integrated system "Reset default"
        self.find_element_byxpath(self.driver, Locators.export_reset_default).click()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        alert.accept()

#Maintenance Tab under property settings
        driver.refresh()  # to refresh current page
        time.sleep(4)
        self.find_element_byxpath(self.driver, '//*[@id="application-settings-app"]/div/div/div[3]/div[3]/div').click()
        time.sleep(5)
# Click on techs
        self.find_element_byxpath(self.driver, '//*[@id="application-settings-app"]/div/div/div[4]/div[1]/div[2]/div/div[1]').click()
#Tech Maps "Switch button turn off"
        self.find_element_byxpath(self.driver,'//*[@id="application-settings-app"]/div/div/div[4]/div[2]').click()
        self.find_element_byxpath(self.driver, '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[1]/div/div/div[2]').click()
        time.sleep(4)
# Tech Maps save button
        self.find_element_byxpath(self.driver, '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/button').click()
        time.sleep(3)
        alert = self.driver.switch_to.alert
        alert.accept()
#Maintenance Tab under property settings
        driver.refresh()
        time.sleep(3)
        self.find_element_byxpath(self.driver, '//*[@id="application-settings-app"]/div/div/div[3]/div[3]/div').click()
        time.sleep(3)
#Export work orders to integrated system "Reset default"
        self.find_element_byxpath(self.driver, '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[1]/div/a').click()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        alert.accept()
#Payment Tab under property managment
        driver.refresh()
        time.sleep(2)
        self.find_element_byxpath(self.driver, '//*[@id="application-settings-app"]/div/div/div[3]/div[5]/div').click()
        time.sleep(3)
#Export Payments switch button turn off
        self.find_element_byxpath(self.driver, '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[1]/div/div/div[2]').click()
        time.sleep(3)
#Export Payments save button
        self.find_element_byxpath(self.driver, '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/button').click()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        alert.accept()
#Payment Tab under property management
        driver.refresh()
        time.sleep(2)
        self.find_element_byxpath(self.driver, '//*[@id="application-settings-app"]/div/div/div[3]/div[5]/div').click()
        time.sleep(3)
#Export Payments rest default
        self.find_element_byxpath(self.driver, '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[1]/div/a').click()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        alert.accept()
#Click on Property settings
        driver.refresh()
        time.sleep(2)
        self.find_element_byxpath(self.driver, '//*[@id="application-settings-app"]/div/div/div[1]/div/div[2]/div').click()
#Click on General tab
driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div/div[3]/div[1]/div').click()
driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div/div[1]/button').click()  #Click on New Property
#Create Property Button
driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div/div[5]/div/div[2]/button').click()   #Create Property Button
driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div/div[5]/div/div[2]/div[2]/input').send_keys('7654')  #Enter Code
driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div/div[5]/div/div[2]/button').click()  #Create Property Button
driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div/div[5]/div/div[2]/div[1]/input').send_keys('johar1 Town')  #Enter property Name
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="application-settings-app"]/div/div/div[5]/div/div[2]/button').click()  #Create Property Button
driver.refresh()
time.sleep(2)



def main():
    loginObject = Utils()
    loginObject.login()
if __name__ == "__main__":
    main()
