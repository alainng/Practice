from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from system import is_program_running
import settings

_browser = None
WEBDRIVERWAITTIMEOUT = 10

def launch_browser(name):
    global _browser
    try:
        if name == "firefox":            
            _browser = webdriver.Firefox(executable_path=r"C:\tests\selenium_drivers\geckodriver.exe")
#                 caps=DesiredCapabilities.FIREFOX
#                 caps["marionette"]=False
#                 _browser = webdriver.Firefox(capabilities=caps)                
        if name == "chrome":
            _browser = webdriver.Chrome(executable_path=r"C:\tests\selenium_drivers\chromedriver.exe")
        if name == "ie":
            _browser = webdriver.Ie(executable_path=r"C:\tests\selenium_drivers\IEDriverServer.exe")
        if name == "edge":
            _browser = webdriver.Edge(executable_path=r"C:\tests\selenium_drivers\MicrosoftWebDriver.exe")
        #_browser.implicitly_wait(15)
        _browser.set_script_timeout(30)
        _browser.set_page_load_timeout(30)
    except WebDriverException as wde:
        print("{} did not open as expected".format(name))
        raise
    except Exception as e:
        print("Unexpected error: {}".format(repr(e)))

def close_browser():
    #note: Firefox Geckodriver has a bug that close() doesn't close it..
    #https://github.com/mozilla/geckodriver/issues/285
    _browser.close()

def quit_browser():
    #note: Firefox geckodriver can quit.. but will produce error: 'NoneType' object has no attribute 'path' 
    #This method does close FF
    _browser.quit()
    return True

def isolate_domain(url):
    words=url.split(".")
    if words[0].find("www"):
        result=words[1]
    else:
        result=words[0]
    return result

def navigate_to(url):
    try:
        _browser.get(url)
    except Exception as e:
        print("Unexpected error: {}".format(repr(e)))

#waittypes https://selenium-python.readthedocs.io/waits.html
def find_element_by_id(id_name):
    try:
        element = WebDriverWait(_browser, WEBDRIVERWAITTIMEOUT).until(EC.visibility_of_element_located((By.ID, id_name)))
    except TimeoutException as te:
        print("No id found {}".format(te))
        raise
    return element

def find_element_by_xpath(xpath):
    try:
        element = WebDriverWait(_browser, WEBDRIVERWAITTIMEOUT).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    except TimeoutException as te:
        print("No element with xpath found {} {}".format(xpath,te))
        raise
    return element


#Dynamic steps below
#action: verb_impl()
#question: is_something_impl()
@when('I launch "{browser}"')
def launch_browser_impl(context,browser):
    launch_browser(browser.lower())
    
@when('I navigate to "{url}"')
def navigate_to_url_impl(context,url):
    navigate_to(url)
    keyword=isolate_domain(url)
    assert _browser.current_url.find(keyword) > 0 , "Mismatched URLs {} cannot find {}".format(_browser.current_url,keyword)

@when('I close the browser')
def close_browser_impl(context):
    close_browser()

@when('I quit the browser')
def quit_browser_impl(context):
    quit_browser()

@then('I find element with id "{input_id}"')
def find_element_by_id_impl(context,input_id):
    assert input_id is not None

@then('I find element with xpath "{input_xpath}"')
def find_element_by_xpath_impl(context,input_xpath):
    assert input_xpath is not None

@then('"{}" is open')
def is_browser_open_impl(context,browser):
    browser_binary_name=settings.get_binary_name(browser)
    assert is_program_running(browser_binary_name) is True, "Browser {} is not running".format(browser_binary_name)
    #assert_true(is_program_running(browser_binary_name), "Browser {} is not running".format(browser_binary_name))

#Static steps below
