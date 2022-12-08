import time
import unittest

from webdriver_manager.chrome import ChromeDriverManager

from Appwork.Utils.Utils import Core
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from Appwork.Locators.locators import Locators
from Appwork.ApplicationSettings.Login import Login

class CoreSystemSettings(unittest.TestCase):
    @classmethod
    def setUp(self):
        #self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://admin.appworkco-beta.com/sessions")
        Core.login(self.driver)

    def test_flow(self):
        Core.navigate(self.driver)
        # self.theme_settings()
        # self.reset_theme()
        self.group_block()

    def theme_settings(self):
        Core.find_element_byxpath(self.driver, Locators.setting_logo_url).click()     # setting logo url
        logo_element = Core.find_element_byxpath(self.driver, Locators.logo_url)
        Core.set_element (logo_element,  'https://www.google.com/', self.driver)  # Application Logo URL
        primary_element = Core.find_element_byxpath(self.driver, Locators.primary_color)
        Core.set_element(primary_element,'#DB0B0B', self.driver)  # Primary Color
        #Core.set_element(Core.find_element_byxpath(self.driver, Locators.secondary_color),'#E6780C', self.driver)  # Secondary Color
        self.assertIsNone(Core.set_element(Core.find_element_byxpath(self.driver, Locators.secondary_color),'#E6780C', self.driver), 'Secondary colour not changed')
        Core.set_element(Core.find_element_byxpath(self.driver, Locators.sidebar_color),'#0F13D8', self.driver)  # Sidebar Color
        Core.set_element(Core.find_element_byxpath(self.driver, Locators.sidebar_text),'#AE1F89', self.driver)  # Sidebar Text Color
        Core.find_element_byxpath(self.driver, Locators.save_button).click()  # To Save theme Setting page)
        time.sleep(2)
        Core.set_alert(self.driver)

    def reset_theme(self):
        Core.find_element_byxpath(self.driver, Locators.rest_logo_url).click()  # Logo Url reset button
        Core.set_alert(self.driver)
        Core.find_element_byxpath(self.driver, Locators.reset_primary).click()  # Reset Primary Color
        Core.set_alert(self.driver)
        Core.find_element_byxpath(self.driver, Locators.reset_secondary).click()  # Reset Secondary Color
        Core.set_alert(self.driver)
        Core.find_element_byxpath(self.driver, Locators.reset_sidebar_color).click()  # Reset Sidebar Color
        Core.set_alert(self.driver)
        Core.find_element_byxpath(self.driver, Locators.reset_sidebar_text).click()  # Reset Sidebar Text Color
        Core.set_alert(self.driver)

    def group_block(self):
        Core.find_element_byxpath(self.driver, Locators.group_block).click()
        Core.find_element_byxpath(self.driver, Locators.new_region).click()
        Core.find_element_byxpath(self.driver, Locators.region_name).send_keys('New Test Region')
        time.sleep(1)
        Core.find_element_byxpath(self.driver, Locators.save_region1).click()
        time.sleep(1)
        Core.find_element_byxpath(self.driver, Locators.click_on_selector).click()
        Core.find_element_byxpath(self.driver, Locators.select_property1).click()
        self.driver.implicitly_wait(5)
        Core.find_element_byxpath(self.driver, Locators.select_property2).click()
        self.driver.implicitly_wait(5)
        Core.find_element_byxpath(self.driver, Locators.search_property1).send_keys('ArborGate Estates')
        Core.find_element_byxpath(self.driver, Locators.click_property1).click()
        self.driver.implicitly_wait(5)
        Core.set_element(Core.find_element_byxpath(self.driver, Locators.search_property1), 'Alera West', self.driver)
        Core.find_element_byxpath(self.driver, Locators.click_property2).click()
        self.driver.implicitly_wait(5)
        Core.find_element_byxpath(self.driver, Locators.change_name).click()
        Core.set_element(Core.find_element_byxpath(self.driver, Locators.update_region), 'Dasman region', self.driver)
        Core.find_element_byxpath(self.driver, Locators.click_done).click
        Core.find_element_byxpath(self.driver, Locators.delete_group).click()

    def tearDown(self):
        self.driver.close()  # Close the browser.
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

