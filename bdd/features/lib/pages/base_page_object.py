from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import traceback

class BasePage(object):
    def __init__(self,driver,url):
        self.driver = driver
        self.url = url
        self.timeout = 30

    def find_element(self, *loc):
        return self.driver.find_element(*loc)
  
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
        #note: Firefox geckodriver can quit.. but will produce error: 'NoneType' object has no attribute 'path' 
        #This method does close FF
        self.driver.quit()