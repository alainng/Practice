from behave import *
from features.lib.pages import *
from features.lib.driver import *
# from selenium.common.exceptions import WebDriverException
# from selenium import webdriver
# 
# class DriverFactory:
#     def getDriver(self,input_name):    
#         name=input_name.lower()
#         try:
#             if name == "ie":
#                 return webdriver.Ie(executable_path=r"C:\selenium_drivers\IEDriverServer.exe")
#             elif name == "edge":
#                 return webdriver.Edge(executable_path=r"C:\selenium_drivers\MicrosoftWebDriver.exe")
#             elif name == "firefox":            
#                 return webdriver.Firefox(executable_path=r"C:\selenium_drivers\geckodriver.exe")          
#             else:
#                 return webdriver.Chrome(executable_path=r"C:\selenium_drivers\chromedriver.exe")
#         except WebDriverException as wde:
#             print("{} did not open as expected".format(wde))
#             raise
#         except Exception as e:
#             print("Unexpected error: {}".format(repr(e)))

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
    googlepage.query("ipad")


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
