from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from system import is_program_running
import settings

class DriverFactory:
    def getDriver(self,input_name):    
        name=input_name.lower()
        try:
            if name == "ie":
                return webdriver.Ie(executable_path=r"C:\selenium_drivers\IEDriverServer.exe")
            elif name == "edge":
                return webdriver.Edge(executable_path=r"C:\selenium_drivers\MicrosoftWebDriver.exe")
            elif name == "firefox":            
                return webdriver.Firefox(executable_path=r"C:\selenium_drivers\geckodriver.exe")          
            else:
                return webdriver.Chrome(executable_path=r"C:\selenium_drivers\chromedriver.exe")
        except WebDriverException as wde:
            print("{} did not open as expected".format(wde))
            raise
        except Exception as e:
            print("Unexpected error: {}".format(repr(e)))

class BasePage(object):
    def __init__(self,driver,url):
        self.driver=driver
        self.url=url

    def find_element_by_id(self,id):
        elem = self.driver.find_element_by_id(id)
        return elem
    
  
    def navigate(self):
        try:
            self.driver.get(self.url)
        except Exception as e:
            print("Unexpected error: {}".format(repr(e)))
    
    def tear_down(self):
        #note: Firefox geckodriver can quit.. but will produce error: 'NoneType' object has no attribute 'path' 
        #This method does close FF
        self.driver.quit()

class GooglePage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, "https://www.google.ca/")
    
    def setQuery(self, query):
        self.fill_form_by_id("lst-ib", query)
    #waittypes https://selenium-python.readthedocs.io/waits.html
#     def find_element_by_id(id_name):
#         try:
#             element = WebDriverWait(_browser, WEBDRIVERWAITTIMEOUT).until(EC.visibility_of_element_located((By.ID, id_name)))
#         except TimeoutException as te:
#             print("No id found {}".format(te))
#             raise
#         return element
#     
#     def find_element_by_xpath(xpath):
#         try:
#             element = WebDriverWait(_browser, WEBDRIVERWAITTIMEOUT).until(EC.visibility_of_element_located((By.XPATH, xpath)))
#         except TimeoutException as te:
#             print("No element with xpath found {} {}".format(xpath,te))
#             raise
#         return element


def create_driver(context,browser):
    drv = getattr(context, "driver", None)
    if not drv:
        return DriverFactory().getDriver(browser)
        
#Dynamic steps below
#action: verb_impl()
#question: is_something_impl()
@when('I launch {browser}')
def launch_browser_impl(context,browser):
    context.driver=create_driver(context,browser)

    
@when('I navigate to {url}')
def navigate_to_url_impl(context,url):
    googlepage=GooglePage(context.driver)
    googlepage.navigate()
    googlepage.setQuery("ipad")


@then('I find element with id "{input_id}"')
# def find_element_by_id_impl(context,input_id):
#     assert input_id is not None
# 
# @then('I find element with xpath "{input_xpath}"')
# def find_element_by_xpath_impl(context,input_xpath):
#     assert input_xpath is not None

@then('{} is open')
def is_browser_open_impl(context,browser):
    browser_binary_name=settings.get_binary_name(browser)
    assert is_program_running(browser_binary_name) is True, "Browser {} is not running".format(browser_binary_name)

#Static steps below
