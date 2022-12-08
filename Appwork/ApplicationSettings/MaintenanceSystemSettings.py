import time
import unittest

from selenium import webdriver
from Appwork.Utils.Utils import Core
from Appwork.Locators.locators import Locators
from webdriver_manager.chrome import ChromeDriverManager

class MaintenanceSystemSettings(unittest.TestCase):
    @classmethod
    def setUp(self):
        #self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://admin.appworkco-beta.com/sessions")
        Core.login(self.driver)
        Core.navigate(self.driver)

    def test_maintenance_tab(self):
        self.assertIsNone(Core.find_element_byxpath(self.driver, Locators.maintenance_tab).click(), "Not clicked on Maintenance Tab")  # Maintenance Tab
        Core.find_element_byxpath(self.driver, Locators.workorder_block).click()  # Click on work order block
        toggle = Core.find_element_byxpath(self.driver, Locators.export_switch_button).get_attribute("value")
        Core.find_element_byxpath(self.driver, Locators.export_switch_button).click()  # Export work orders to integrated system "Switch button turn off"
        toggle1 = Core.find_element_byxpath(self.driver, Locators.export_switch_button).get_attribute("value")
        self.assertNotEqual(toggle, toggle1, 'Toggle not working')
        time.sleep(2)
        Core.find_element_byxpath(self.driver, Locators.save_export).click()  # Export Work Orders save button
        Core.set_alert(self.driver)
        Core.driver_refresh(self.driver)
        Core.find_element_byxpath(self.driver, Locators.maintenance_tab).click()  # Maintenance Tab under property settings
        Core.find_element_byxpath(self.driver, Locators.export_reset_default).click()
        Core.set_alert(self.driver)
        Core.driver_refresh(self.driver)  # to refresh current page
        Core.find_element_byxpath(self.driver, Locators.maintenance_tab).click()  # Maintenance Tab under property settings
        Core.find_element_byxpath(self.driver, Locators.techs_block).click()  # Click on techs
        Core.find_element_byxpath(self.driver, Locators.maps_switch).click()  # Tech Maps Switch button turn off
        # Core.find_element_byxpath(self.driver, Locators.maps_switch_button).click()
        Core.find_element_byxpath(self.driver, Locators.tech_save).click()  # Save Tech Block
        Core.set_alert(self.driver)
        Core.find_element_byxpath(self.driver, Locators.maintenance_tab).click()  # Maintenance Tab under property settings
        time.sleep(1)
        Core.find_element_byxpath(self.driver, Locators.techs_block).click()  # Click on techs
        time.sleep(1)
        Core.find_element_byxpath(self.driver, Locators.reset_tech_maps).click()  # Export work orders to integrated system "Reset default"
        Core.set_alert(self.driver)

    def tearDown(self):
        self.driver.close()  # Close the browser.
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
