from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import traceback
import re
from urlparse import urlparse, parse_qs

class BasePage(object):
    def __init__(self,driver,url):
        self.driver = driver
        self.url = url
        self.timeout = 30

    def find_element(self, *loc):
        return self.driver.find_element(*loc)
    
    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)
    
    def find_element_parent(self, *loc):
        currentElement=self.driver.find_element(*loc)        
        return currentElement.find_element_by_xpath("..")

    def get_element_text(self, *loc):
        return self.driver.find_element(*loc).text
    
    #returns a dict of lists
    def get_parsed_current_url(self):
        return parse_qs(urlparse(self.driver.current_url).query,keep_blank_values=True)
    
    #return boolean
    def match_current_url_with_regex(self,regex):
        return re.search(regex,self.driver.current_url)

    def navigate(self):
        self.driver.get(self.url)

    def __getattr__(self, what):
        try:
            if what in self.locator_dictionary.keys():
                try:
                    element = WebDriverWait(self.driver,self.timeout).until(
                        EC.presence_of_element_located(self.locator_dictionary[what])
                    )
                except(TimeoutException,StaleElementReferenceException):
                    traceback.print_exc()

                try:
                    element = WebDriverWait(self.driver,self.timeout).until(
                        EC.visibility_of_element_located(self.locator_dictionary[what])
                    )
                except(TimeoutException,StaleElementReferenceException):
                    traceback.print_exc()
                # I could have returned element, however because of lazy loading, I am seeking the element before return
                return self.find_element(*self.locator_dictionary[what])
        except AttributeError:
            super(BasePage, self).__getattribute__("method_missing")(what)

    def method_missing(self, what):
        print "No %s here!"%what
    
    def tear_down(self):
        if self.driver is not None:
            self.driver.close()
        if self.driver is not None:
            self.driver.quit()