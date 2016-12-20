from selenium.webdriver.common.by import By
from base_page_object import BasePage
import time
import re


class HomePage(BasePage):
    locator_dictionary = {
        #compound classes need to be found by css_selector
        #http://stackoverflow.com/questions/17808521/how-to-avoid-compound-class-name-error-in-page-object
        
        #reservationShared
        "reservationCitySearchBox": (By.CSS_SELECTOR, ".form-control.js-search_address"), #if you choose to toggle between now and later, the info stays
        "ifSearchMapElementLoaded": (By.XPATH, "//div[@class='search-map']"),   
     
        #reservationNow
        "reservationNowTab": (By.XPATH,"//div[@class='searchbox__type btn-group']/label"),
        "reservationNowDuration": (By.XPATH, "//select[@name='duration']/option[@value='2']"), # 1,2,4,6,8,10,12
        "reservationNowRechercherButton": (By.XPATH, "//div[@data-visibility-slave='now']/button"),
        
        #reservationLater
        "reservationLaterTab": (By.XPATH,"//div[@class='searchbox__type btn-group']/label"),
        "reservationLaterRechercherButton": (By.XPATH, "//div[@data-visibility-slave='later']/button"),
        "reservationCurrentLocationButton": (By.CSS_SELECTOR, ".searchbox__geolocate.js-geolocate"), #TODO:unused because i might need to grant location access
        "reservationLocationRequiredErrorMessage": (By.XPATH, "//div[@id='parsley-location-errors']/ul/li"),
    }

    def __init__(self, driver):
        BasePage.__init__(
            self,
            driver,
            "https://www.koolicar.com")

    def click_locator(self,locator):
        self.find_element(*self.locator_dictionary[locator]).click()
    
    def send_keys_locator(self,locator,query):
        self.find_element(*self.locator_dictionary[locator]).send_keys(query)
    
    def later_reservation(self):
        query="france"
        startDate=None
        startHour=None
        endDate=None
        endHour=None
        
        self.find_elements(*self.locator_dictionary["reservationLaterTab"])[1].click()
        self.send_keys_locator("reservationCitySearchBox",query)
        self.click_locator("reservationLaterRechercherButton")
        time.sleep(2)
        if query == "":
            assert self.find_element(*self.locator_dictionary["reservationLocationRequiredErrorMessage"]) is not None, "Error message is not displaying for empty search"
        else:
            assert self.find_element(*self.locator_dictionary["ifSearchMapElementLoaded"]) is not None, "Page never loaded after 30s"  #Wait for page to load
            parsed_url=self.get_parsed_current_url()    #dictionary of lists
            assert parsed_url["search_options"][0]=="later", "Missing search_options parameter: {}".format(parsed_url["search_options"][0])
            assert parsed_url["search[address]"][0]==query,"Missing search[address] parameter: {}".format(parsed_url["search[address]"][0])
    
    def later_reservation_current_location(self):
        startDate=None
        startHour=None
        endDate=None
        endHour=None
        
        self.find_elements(*self.locator_dictionary["reservationLaterTab"])[1].click()
        self.click_locator("reservationCurrentLocationButton")
        self.click_locator("reservationLaterRechercherButton")    
        time.sleep(2)
        assert self.find_element(*self.locator_dictionary["ifSearchMapElementLoaded"]) is not None, "Page never loaded after 30s"  #Wait for page to load
        parsed_url=self.get_parsed_current_url()    #dictionary of lists
        assert parsed_url["search_options"][0]=="later", "Missing search_options parameter: {}".format(parsed_url["search_options"][0])
        
    
    def now_reservation(self):
        query="france"
        
        self.find_elements(*self.locator_dictionary["reservationNowTab"])[0].click()
        self.send_keys_locator("reservationCitySearchBox",query)
        self.click_locator("reservationNowDuration")
        self.click_locator("reservationNowRechercherButton")
        time.sleep(2)
        if query == "":
            assert self.find_element(*self.locator_dictionary["reservationLocationRequiredErrorMessage"]) is not None, "Error message is not displaying for empty search"
        else:
            assert self.find_element(*self.locator_dictionary["ifSearchMapElementLoaded"]) is not None, "Page never loaded after 30s"  #Wait for page to load
            parsed_url=self.get_parsed_current_url()    #dictionary of lists
            assert parsed_url["search_options"][0]=="immediate", "Missing search_options parameter: {}".format(parsed_url["search_options"][0])
            assert parsed_url["search[address]"][0]==query,"Missing search[address] parameter: {}".format(parsed_url["search[address]"][0])

    def test_reservation_form(self):
        self.now_reservation()
        