from selenium import webdriver
from faker import Faker
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import page
import os


DRIVER_PATH = os.getcwd() + "/drivers/chromedriver"

class SogetiTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(DRIVER_PATH)
        self.driver.get("https://sogeti.com")
        self.driver.implicitly_wait(10) # seconds
        WebDriverWait(self.driver, 10).until(
            lambda wd: 'complete' == (self.driver.execute_script("return document.readyState;"))
        )


    def test_automation_page(self):
        mainPage = page.MainPage(self.driver)
        mainPage.hover_over_services()
        mainPage.click_automation_link()
        automationPage = page.AutomationPage(self.driver)
        assert automationPage.is_automation_page()
        assert automationPage.is_automation_selected()
    

    def test_automation_form(self):
        mainPage = page.MainPage(self.driver)
        mainPage.hover_over_services()
        mainPage.click_automation_link()
        automationPage = page.AutomationPage(self.driver)
        automationPage.scroll_to_contactform()
        
        # fill out the form with fake data
        f = Faker()
        fullname = f.name().split(" ")
        automationPage.fname = fullname[0]
        automationPage.lname = fullname[1]
        automationPage.email = f.email()
        automationPage.phone = f.phone_number()
        automationPage.message = "Example Message"
        
        automationPage.send_the_form()
        assert automationPage.is_message_sent()


    def test_country_list(self):
        mainPage = page.MainPage(self.driver)
        mainPage.is_country_list_ok()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()