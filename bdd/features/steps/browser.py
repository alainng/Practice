from behave import *
from selenium import webdriver
from nose.tools import assert_raises, assert_true, assert_false
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

_browser = None

def open_browser(name):
    global _browser
    try:
        if name == "Firefox":
            _browser = webdriver.Firefox(executable_path=r"C:\tests\selenium_drivers\geckodriver.exe")
            #If you need Firefox <=47 support: 
            #caps=DesiredCapabilities.FIREFOX
            #caps["marionette"]=False
            #_browser = webdriver.Firefox(capabilities=caps)
        if name == "Chrome":
            _browser = webdriver.Chrome(executable_path=r"C:\tests\selenium_drivers\chromedriver.exe")
        if name == "Ie":
            _browser = webdriver.Ie(executable_path=r"C:\tests\selenium_drivers\IEDriverServer.exe")
    except Exception as e:
        print("Unexpected error: {}".format(repr(e)))

def visit_url(url):
    try:
        _browser.get(url)
    except Exception as e:
        print("Unexpected error: {}".format(repr(e)))
        
@given("Chrome is installed")
def is_chrome_installed(context):
    open_browser("Chrome")
    visit_url("https://www.google.com")
    return True

@when("I launch Chrome")
def launch_browser(context):
    open_browser("Chrome")
    

@then("Chrome is open")
def browser_is_open(context):
    return True
