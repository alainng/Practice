from selenium.webdriver.common.by import By
from base_page_object import BasePage


class GooglePage(BasePage):
    locator_dictionary = {
        "searchBox": (By.ID, 'lst-ib'),
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            'https://www.google.ca/')

    def login(self,query="ipad"):
        self.find_element(*self.locator_dictionary['searchBox']).send_keys(query)