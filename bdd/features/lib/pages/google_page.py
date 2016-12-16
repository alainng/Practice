from selenium.webdriver.common.by import By
from base_page_object import BasePage


class GooglePage(BasePage):
    locator_dictionary = {
        "searchBox": (By.ID, 'lst-ib'),
    }

    def __init__(self, driver):
        BasePage.__init__(
            self,
            driver,
            'https://www.google.ca/')

    def query(self,query):
        self.find_element(*self.locator_dictionary['searchBox']).send_keys(query)