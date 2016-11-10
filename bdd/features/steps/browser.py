from behave import *
from selenium import webdriver
from nose.tools import assert_raises, assert_true, assert_false

#_browser = None

def open_browser(name):
    try:
        if name == "Chrome":
            _browser = webdriver.Chrome(executable_path="C:\\tests\bdd\selenium_drivers\\chromedriver.exe", service_args=["--verbose", "--log-path=c:\\chromedriver.log"])
        _browser.set_page_load_timeout(60) #deadcode?
    except Exception as e:
        print("Unexpected error: {}".format(repr(e)))
    return _browser

@given("Chrome is installed")
def is_chrome_installed(context):
    browser=open_browser("Chrome")
    browser.geturl("https://www.google.com")
    return True

@when("I launch Chrome")
def launch_browser(context):
    
    return True
    

@then("Chrome is open")
def browser_is_open(context):
    return True
