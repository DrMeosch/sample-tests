from locator import MainPageLocators
from element import BasePageElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FirstNameElement(BasePageElement):
    locator = "4ff2ed4d-4861-4914-86eb-87dfa65876d8"

class LastNameElement(BasePageElement):
    locator = "11ce8b49-5298-491a-aebe-d0900d6f49a7"

class EmailElement(BasePageElement):
    locator = "056d8435-4d06-44f3-896a-d7b0bf4d37b2"

class PhoneElement(BasePageElement):
    locator = "755aa064-7be2-432b-b8a2-805b5f4f9384"

class MessageElement(BasePageElement):
    locator = "88459d00-b812-459a-99e4-5dc6eff2aa19"


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    def hover_over_services(self):
        # services = self.driver.find_element(*MainPageLocators.SERVICES)
        services = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.SERVICES)
        )
        actions = ActionChains(self.driver)
        services.click()
        # Stable
        actions.move_to_element(services).pause(3).perform()
        return services


    def click_automation_link(self):
        # automation = self.driver.find_element(*MainPageLocators.AUTOMATION)
        automation = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.AUTOMATION)
        )
        automation.click()


    def is_country_list_ok(self):
        l = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.COUNTRY_LIST)
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(l).perform()
        l.click()
        countries = self.driver.find_elements(*MainPageLocators.COUNTRIES)
        links = [country.get_attribute("href") for country in countries]
        for lnk in links:
            self.driver.get(lnk)
            if self.driver.title is None:
                return False
        return True

class AutomationPage(MainPage):
    
    fname = FirstNameElement()
    lname = LastNameElement()
    email = EmailElement()
    phone = PhoneElement()
    message = MessageElement()

    def is_automation_page(self):
        return ("Automation" in self.driver.title and \
            "Automation" in self.driver.find_element(*MainPageLocators.VISIBLE).text)

    def is_automation_selected(self):
        services = self.hover_over_services()
        attr_1 = services.find_element_by_xpath('./../..').get_attribute("class")
        automation = self.driver.find_element(*MainPageLocators.AUTOMATION)
        attr_2 = automation.find_element_by_xpath('./..').get_attribute("class")
        return ("selected" in attr_1 and "selected" in attr_2)

    def scroll_to_contactform(self):
        contact_form = self.driver.find_element(*MainPageLocators.CONTACT_FORM)
        self.driver.execute_script("arguments[0].scrollIntoView();", contact_form)
    

    def send_the_form(self):
        i_agree = self.driver.find_element(*MainPageLocators.I_AGREE)
        i_agree.click()
        submit = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.SUBMIT_FORM)
        )
        submit.click()


    def is_message_sent(self):
        msg = self.driver.find_element(*MainPageLocators.MSG)
        return ("Thank you for contacting us." in msg.text)