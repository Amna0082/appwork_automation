import warnings
import unittest

from Appwork.Locators.locators import Locators
from Appwork.Utils.Utils import Core
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

class Login(unittest.TestCase):
    @classmethod
    def setUp(self):
        #self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://admin.appworkco-beta.com/sessions")

    def test_invalid_login(self):
        Core.find_element_byid(self.driver, Locators.email_input).send_keys('1talha@invozone.com')
        Core.find_element_byid(self.driver, Locators.password_input).send_keys('1p@ssw0rd#!')
        Core.find_element_byxpath(self.driver, Locators.login_button).click()
        errors = Core.find_element_byxpath(self.driver, Locators.error_message)
        error_message = "Invalid Login"
        self.assertEquals(error_message, errors, "Invalid Login" )

    def test_logout(self):
        Core.find_element_byid(self.driver, Locators.email_input).send_keys('talha@invozone.com')  # email field
        Core.find_element_byid(self.driver, Locators.password_input).send_keys('p@ssw0rd#!')  # password field
        Core.find_element_byxpath(self.driver, Locators.login_button).click()  # click on login button
        Core.find_element_byxpath(self.driver, Locators.sidebar_app).click()
        Core.find_element_byxpath(self.driver, Locators.sidebar_popup).click()
        Core.find_element_byxpath(self.driver, Locators.logout).click()
        get_url = self.driver.current_url
        self.assertEquals('https://admin.appworkco-beta.com/sessions', get_url, 'Not Logout' )

    def test_success_login(self):
        Core.find_element_byid(self.driver, Locators.email_input).send_keys('talha@invozone.com')  # email field
        Core.find_element_byid(self.driver, Locators.password_input).send_keys('p@ssw0rd#!')  # password field
        Core.find_element_byxpath(self.driver, Locators.login_button).click()  # click on login button
        get_url = self.driver.current_url
        self.assertEquals('https://admin.appworkco-beta.com/', get_url, 'Not Logout')

    def tearDown(self):
        self.driver.close()  # Close the browser.
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()




