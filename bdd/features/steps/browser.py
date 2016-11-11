from behave import *
from selenium import webdriver
from nose.tools import assert_raises, assert_true, assert_false
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from system import is_program_running
import settings

_browser = None

def launch_browser(name):
    global _browser
    try:
        if name == "firefox":
            _browser = webdriver.Firefox(executable_path=r"C:\tests\selenium_drivers\geckodriver.exe")
            ##If you need Firefox <=47 support: 
            #caps=DesiredCapabilities.FIREFOX
            #caps["marionette"]=False
            #_browser = webdriver.Firefox(capabilities=caps)
        if name == "chrome":
            _browser = webdriver.Chrome(executable_path=r"C:\tests\selenium_drivers\chromedriver.exe")
        if name == "ie":
            _browser = webdriver.Ie(executable_path=r"C:\tests\selenium_drivers\IEDriverServer.exe")
        _browser.implicitly_wait(15)
        _browser.set_script_timeout(30)
        _browser.set_page_load_timeout(30)
    except Exception as e:
        print("Unexpected error: {}".format(repr(e)))

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

#Dynamic steps below  
@when("I launch {browser}")
def launch_browser_impl(context,browser):
    launch_browser(browser.lower())
    
@when("I navigate to {url}")
def navigate_to_url_impl(context,url):
    navigate_to(url)
    keyword=isolate_domain(url)
    assert_true(_browser.current_url.find(keyword),"Mismatched URLs {} cannot find {}".format(_browser.current_url,keyword))

@then("Chrome is open")
def browser_is_open(context):
    assert_true(is_program_running("chrome.exe"), "Browser {} is not running".format("chrome.exe"))

#Static steps below