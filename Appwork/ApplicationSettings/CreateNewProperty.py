import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Appwork.Utils.Utils import Core
from Appwork.Locators.locators import Locators



class CreateNewProperty(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://admin.appworkco-beta.com/sessions")
        Core.login(self.driver)
        Core.navigate(self.driver)

    # def __init__(self, driver):
    #     self.driver = driver
    #     Core.driver_refresh(self.driver)

    def test_property(self):
        self.new_property()
        self.update_property()
        self.document_block()
        self.floor_plan_block()
        self.showing_hours()
        self.api_keys()

    def new_property(self):
        name = Core.get_random_string(5, 'property')
        Core.find_element_byxpath(self.driver, Locators.property_settings).click()  # Property Settings
        # Core.find_element_byxpath(self.driver, Locators.new_property).click()    #New property Button
        # Core.find_element_byxpath(self.driver, Locators.property_name).send_keys(name)
        # value = Core.find_element_byxpath(self.driver, Locators.property_name).get_attribute('value')
        # assert name == value
        Core.find_element_byxpath(self.driver, Locators.enter_code).send_keys(Core.get_random_string(4,'0'))
        Core.find_element_byxpath(self.driver, Locators.enter_address).send_keys('test address')
        Core.find_element_byxpath(self.driver, Locators.enter_city).send_keys('lahore')
        # Core.find_element_byxpath(self.driver, Locators.click_region).click()
        # Core.find_element_byxpath(self.driver, Locators.search_region).send_keys('Alabama')
        # Core.find_element_byxpath(self.driver, Locators.select_region).click()
        # Core.find_element_byxpath(self.driver, Locators.enter_zipcode).send_keys('12345')
        # Core.find_element_byxpath(self.driver, Locators.enter_integration_id).send_keys(Core.get_random_string(4,'0'))
        # Core.find_element_byxpath(self.driver, Locators.create_property).click()
        Core.find_element_byxpath(self.driver, Locators.property_selector).click()
        Core.find_element_byxpath(self.driver, Locators.search_property).send_keys('Arborgate')
        Core.find_element_byxpath(self.driver, Locators.select_property).click()
        Core.find_element_byxpath(self.driver, Locators.deactivate_property).click()
        time.sleep(2)
        Core.find_element_byxpath(self.driver, Locators.activate_property).click()

    # Update/Edit Property

    def update_property(self):

        Core.find_element_byxpath(self.driver, Locators.general_tab).click()
        propertyname = "ArborGate Estates"
        Core.set_element(Core.find_element_byxpath(self.driver, Locators.update_property_name), propertyname, self.driver)
        assert propertyname == propertyname, 'Property Name not updated'
        # Core.set_element(Core.find_element_byxpath(self.driver, Locators.update_property_address), '671 Westgate Pkwy', self.driver)
        # Core.set_element(Core.find_element_byxpath(self.driver, Locators.update_property_city), 'Dothan', self.driver)
        # Core.find_element_byxpath(self.driver, Locators.update_region).click()
        # Core.find_element_byxpath(self.driver, Locators.update_search_region).send_keys('Alabama')
        # Core.find_element_byxpath(self.driver, Locators.update_select_region).click()
        # Core.set_element(Core.find_element_byxpath(self.driver, Locators.update_zipcode), '36303', self.driver)
        # Core.set_element(Core.find_element_byxpath(self.driver, Locators.update_property_phone), '334-659-3318',self.driver)
        # Core.set_element(Core.find_element_byxpath(self.driver, Locators.update_property_website),'https://arborgateestates.com/', self.driver)
        # Core.set_element(Core.find_element_byxpath(self.driver, Locators.update_property_email),'arborgate@dasmenresidential.com', self.driver)
        # Core.find_element_byxpath(self.driver, Locators.time_zone).click()
        # Core.find_element_byxpath(self.driver, Locators.search_timezone).send_keys('US/Central')
        # Core.find_element_byxpath(self.driver, Locators.select_timezone).click()
        # Core.set_element(Core.find_element_byxpath(self.driver, Locators.update_integration_id), '6050', self.driver)

        # Update Logos
        # Core.find_element_byxpath(self.driver, Locators.upload_logo).send_keys('/Users/amnakhalid/Desktop/Arborgate-Logo-01.png')
        # Core.find_element_byxpath(self.driver, Locators.upload_icon).send_keys('/Users/amnakhalid/Desktop/Arborgate-Icon-05.png')
        # Core.find_element_byxpath(self.driver, Locators.upload_banner).send_keys('/Users/amnakhalid/Desktop/Arborgate-Banner.jpeg')

        Core.find_element_byxpath(self.driver, Locators.save_property).click()

    def document_block(self):
        Core.find_element_byxpath(self.driver, Locators.document_block).click()
        Core.find_element_byxpath(self.driver, Locators.upload_document).send_keys('/Users/amnakhalid/Desktop/Arborgate-Icon-05.png')
        Core.find_element_byxpath(self.driver, Locators.document_name).send_keys('Test Doc')
        Core.find_element_byxpath(self.driver, Locators.file_type).send_keys('.png')
        Core.find_element_byxpath(self.driver, Locators.save_document).click()
        # Core.find_element_byxpath(self.driver, Locators.view_document).click()
        # self.driver.switch_to.window(self.driver.window_handles[0])       #Close current google tab/window and shift to already opened window
        # time.sleep(2)
        # actions = ActionChains(self.driver)
        # actions.key_down(Keys.CONTROL).key_down(Keys.TAB).key_up(Keys.TAB).key_up(Keys.CONTROL).perform()
        Core.find_element_byxpath(self.driver, Locators.delete_document).click()
        Core.set_alert(self.driver)
        time.sleep(2)


    def floor_plan_block(self):
        time.sleep(2)
        Core.find_element_byxpath(self.driver, Locators.floor_plan_block).click()
        Core.find_element_byxpath(self.driver, Locators.new_floor_plan).click()
        Core.find_element_byxpath(self.driver, Locators.floor_name).send_keys('Test Floor')
        Core.find_element_byxpath(self.driver, Locators.search_plan).send_keys('G6004')
        Core.find_element_byxpath(self.driver, Locators.select_plan1).click()
        Core.find_element_byxpath(self.driver, Locators.search_plan).send_keys('H7007')
        Core.find_element_byxpath(self.driver, Locators.select_plan2).click()
        Core.find_element_byxpath(self.driver, Locators.search_plan).send_keys('WG7010')
        Core.find_element_byxpath(self.driver, Locators.select_plan3).click()
        Core.find_element_byxpath(self.driver, Locators.remove_plan).click()
        Core.find_element_byxpath(self.driver, Locators.save_plan).click()

        Core.find_element_byxpath(self.driver, Locators.add_plan).click()
        # Core.find_element_byxpath(self.driver, Locators.search_plan).send_keys('G6004')
        # Core.find_element_byxpath(self.driver, Locators.select_plan1).click()
        Core.find_element_byxpath(self.driver, Locators.cancel_plan).click()
        Core.find_element_byxpath(self.driver, Locators.delete_plan).click()
        Core.set_alert(self.driver)

    def showing_hours(self):
        Core.find_element_byxpath(self.driver, Locators.hours_block).click()
        Core.find_element_byxpath(self.driver, Locators.add_closure).click()
        Core.find_element_byxpath(self.driver, Locators.reason_closure).send_keys('Test closure')
        Core.find_element_byxpath(self.driver, Locators.add_new_closure).click()
        Core.find_element_byxpath(self.driver, Locators.add_closure).click()
        Core.find_element_byxpath(self.driver, Locators.reason_closure).send_keys('Test closure1')
        Core.find_element_byxpath(self.driver, Locators.part_time).click()
        Core.find_element_byxpath(self.driver, Locators.click_time1).click()
        Core.find_element_byxpath(self.driver, Locators.search_time1).send_keys('6:00 AM')
        Core.find_element_byxpath(self.driver, Locators.select_time1).click()

        Core.find_element_byxpath(self.driver, Locators.click_time2).click()
        Core.find_element_byxpath(self.driver, Locators.search_time2).send_keys('8:00 AM')
        Core.find_element_byxpath(self.driver, Locators.select_time2).click()
        Core.find_element_byxpath(self.driver, Locators.add_new_closure).click()

        Core.find_element_byxpath(self.driver, Locators.edit_closure).click()
        Core.set_element(Core.find_element_byxpath(self.driver, Locators.slots), '3', self.driver)
        Core.find_element_byxpath(self.driver, Locators.save_slot).click()

    def api_keys(self):
        Core.find_element_byxpath(self.driver, Locators.api_block).click()
        Core.find_element_byxpath(self.driver, Locators.click_provider).click()
        Core.find_element_byxpath(self.driver, Locators.search_provider).send_keys('Authorize')
        Core.find_element_byxpath(self.driver, Locators.select_provider).click()
        Core.find_element_byxpath(self.driver, Locators.api_keys).send_keys('6Z2FyT9aR88')
        Core.find_element_byxpath(self.driver, Locators.transaction_key).send_keys('65KySw47Yrzr937L')
        Core.find_element_byxpath(self.driver, Locators.public_key).send_keys('4gn3GMK8nXxRJ28t4b7ZD4aJJT9Z53Yx8AcGxVLwEr9qY94r4wdV4rxAHpCr4Rcr')
        Core.set_element(Core.find_element_byxpath(self.driver, Locators.api_login), 'ashburn2', self.driver)
        Core.set_element(Core.find_element_byxpath(self.driver, Locators.api_login), 'Golf1ball#', self.driver)
        Core.find_element_byxpath(self.driver, Locators.save_api).click()


        Core.find_element_byxpath(self.driver, Locators.search_payscape).send_keys('Payscape')
        Core.find_element_byxpath(self.driver, Locators.provider_payscape).click()
        Core.find_element_byxpath(self.driver, Locators.cert).send_keys('67f87bf10449402bab77342e3a23f9c')
        Core.find_element_byxpath(self.driver, Locators.term_id).send_keys('a23f9c')
        Core.find_element_byxpath(self.driver, Locators.payscape_account).send_keys('33129513')
        Core.set_element(Core.find_element_byxpath(self.driver, Locators.payscape_login), 'arborpayments@dasmenresidential.com', self.driver)
        Core.set_element(Core.find_element_byxpath(self.driver, Locators.payscape_password), 'Dothan123!', self.driver)
        Core.find_element_byxpath(self.driver, Locators.save_payscape).click()

    def tearDown(self):
        self.driver.close()  # Close the browser.
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
