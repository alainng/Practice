from selenium.webdriver.common.by import By
from base_page_object import BasePage


class HomePage(BasePage):
    locator_dictionary = {
        "mainLogo": (By.CLASS_NAME, 'navbar-header'),
    }

    def __init__(self, driver):
        BasePage.__init__(
            self,
            driver,
            'https://www.koolicar.com')

    def click_logo(self):
        self.find_element(*self.locator_dictionary['mainLogo']).click()