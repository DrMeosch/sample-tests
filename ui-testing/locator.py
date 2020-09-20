from selenium.webdriver.common.by import By

class MainPageLocators(object):
    SERVICES = (By.XPATH, '//span[text()="Services"]')
    AUTOMATION = (By.LINK_TEXT, 'Automation')
    VISIBLE = (By.XPATH, '//*[contains(.,.)]')
    CONTACT_FORM = (By.XPATH, '//div[@class="Form__Status"]')
    I_AGREE = (By.NAME, "__field_123935")
    SUBMIT_FORM = (By.ID, "06838eea-8980-4305-83d0-42236fb4d528")
    MSG = (By.XPATH, '//div[@class="Form__Status__Message Form__Success__Message"]/p')
    COUNTRY_LIST = (By.XPATH, '//span[text()="Worldwide"]')
    COUNTRIES = (By.XPATH, "//div[@class='country-list']/ul/li/a")