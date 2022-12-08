import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string

from Appwork.Locators.locators import Locators

class Core():
    def set_alert(driver):
        time.sleep(2)
        alert = driver.switch_to.alert.accept()
    def driver_refresh(driver):

        driver.refresh()

    def find_element_byid(driver, id):
        time.sleep(1)
        return driver.find_element(By.ID, id)

    def find_element_byxpath(driver, xpath):
        time.sleep(1)
        return driver.find_element(By.XPATH, xpath)

    def find_element_byclassname(driver, classname):
        time.sleep(1)
        return driver.find_element(By.CLASS_NAME, classname)

        # while not wait.until(element):
        #     self.loading_container(driver, element)
        # try:
        #     element = WebDriverWait(driver, 10).until(element)
        # finally:
        #     driver.quit()

    def login(driver):
        Core.find_element_byid(driver, Locators.email_input).send_keys('talha@invozone.com')  # email field
        Core.find_element_byid(driver, Locators.password_input).send_keys('p@ssw0rd#!')  # password field
        Core.find_element_byxpath(driver, Locators.login_button).click()  # click on login button

    def navigate(driver):
        Core.find_element_byxpath(driver, Locators.sidebar_app).click()
        Core.find_element_byxpath(driver, Locators.sidebar_popup).click()  # sidebar popup
        Core.find_element_byxpath(driver, Locators.settings_button).click()
        time.sleep(2)
        Core.find_element_byxpath(driver, Locators.application_settings).click() # application settings
        time.sleep(2)



    def set_element(element, value, driver = None):
        time.sleep(1)
        if driver:
            driver.execute_script("arguments[0].value = ''", element)
        else:
            element.clear()
        return element.send_keys(value)


    def get_random_string(length, type):
        # choose from all lowercase letter
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return type+' '+result_str


    def wait_till_available(self, driver, xpath):
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

    def wait_till_disappear(self, driver, xpath):
        wait = WebDriverWait(driver, 10)
        wait.until(EC.invisibility_of_element_located((By.XPATH, xpath)))




