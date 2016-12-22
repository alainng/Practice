from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from base_page_object import BasePage
import time
import re

#PageObject Google example: https://github.com/SeleniumHQ/selenium/blob/master/py/test/selenium/webdriver/common/google_one_box.py

class RecherchePage(BasePage):
    locator_dictionary = {
        
    }

    def __init__(self, driver):
        BasePage.__init__(
            self,
            driver,
            "https://www.koolicar.com/recherche?utf8=%E2%9C%93&search_options=later&search%5Baddress%5D=France&search%5Blat%5D=46.227638&search%5Blng%5D=2.213749000000007&search%5Btypes%5D=country%2Cpolitical&search%5Bformatted_address%5D=France&search%5Bcity%5D=&search%5Bstart_string%5D=&search%5Bstart_time%5D=&search%5Bend_string%5D=&search%5Bend_time%5D=")

    def create_request_url(self):
        assert False
    
    
    def is_loaded(self):
        try:
            self.find_element(*self.locator_dictionary["search_section"])
            self.logger.info("Page loaded: {}".format(self.get_current_url()))
            return True
        except NoSuchElementException:
            self.logger.debug("Page did not load properly. Missing element: {}".format("search_section"))
            return False
    
    def locator_click(self,locator):
        self.find_element(*self.locator_dictionary[locator]).click()
    
    def locator_send_keys(self,locator,query):
        self.find_element(*self.locator_dictionary[locator]).send_keys(query)
    
