from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options

import unittest

from Appwork.ApplicationSettings.CoreSystemSettings import CoreSystemSettings
from Appwork.ApplicationSettings.Login import Login
from Appwork.ApplicationSettings.MaintenanceSystemSettings import MaintenanceSystemSettings
from Appwork.ApplicationSettings.CreateNewProperty import CreateNewProperty
from Appwork.ApplicationSettings.PaymentsSystemSettings import PaymentsSystemSettings

class AppRentTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # driver = webdriver.Chrome()
        opt = Options()
        opt.add_argument("--disable-infobars")
        opt.add_argument("start-maximized")
        opt.add_argument("--disable-extensions")
        # Pass the argument 1 to allow and 2 to block
        opt.add_experimental_option("prefs", {
            "profile.default_content_setting_values.media_stream_camera": 1,
        })
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=opt)
        driver.get("https://admin.appworkco-beta.com/sessions")
        cls.driver = driver


    def test_login(self):
        loginobject = Login(self.driver)
        loginobject.success_login()

    def test_core_system_settings(self):
        loginobject = Login(self.driver)
        loginobject.success_login()
        CSS = CoreSystemSettings(self.driver)
        CSS.navigate()
        # CSS.theme_settings()
        # CSS.reset_theme()
        # MSS = MaintenanceSystemSettings(driver)
        # MSS.maintenance_tab()
        # PSS = PaymentsSystemSettings(driver)
        # PSS.payments_tab()
        CNP = CreateNewProperty(self.driver)
        CNP.new_property()
        CNP.update_property()
        # CNP.document_block()
        CNP.floor_plan_block()
        CNP.showing_hours()
        CNP.api_keys()

    # def test_main(self):
    #     driver = self.driver()
        # self.test_core_system_settings(driver)
        # print("Chose from menu")
        # print("1- Core System settings")
        # print("2- Test login")
        # print("0- Quit")
        # print(sys.argv)
        # if len(sys.argv)  1:
        #     while sys.argv[1] != "0":
        # print(sys.argv)
        # if sys.argv[1] == "1":
        # if sys.argv[1] == "2":
        #     test_login()

if __name__ == '__main__':
    unittest.main()
    