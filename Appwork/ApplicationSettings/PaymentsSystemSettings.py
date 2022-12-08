import time
import unittest
from selenium import webdriver
from Appwork.Utils.Utils import Core
from Appwork.Locators.locators import Locators

class PaymentsSystemSettings(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://admin.appworkco-beta.com/sessions")
        Core.login(self.driver)
        Core.navigate(self.driver)

    def test_payments_tab(self):
        Core.find_element_byxpath(self.driver, Locators.payment_tab).click()    #payment tab
        Core.find_element_byxpath(self.driver, Locators.export_payment).click()    #export payment switch button
        Core.find_element_byxpath(self.driver, Locators.save_payment).click()
        Core.set_alert(self.driver)
        Core.driver_refresh(self.driver)
        Core.find_element_byxpath(self.driver, Locators.payment_tab).click()  # payment tab
        Core.find_element_byxpath(self.driver, Locators.reset_payment).click()
        Core.set_alert(self.driver)
        Core.driver_refresh(self.driver)
        Core.find_element_byxpath(self.driver, Locators.payment_tab).click()  # payment tab

    def tearDown(self):
        self.driver.close()  # Close the browser.
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

