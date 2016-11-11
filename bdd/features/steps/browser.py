from behave import *
from selenium import webdriver
from nose.tools import assert_raises, assert_true, assert_false
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from system import is_program_running
import settings

_browser = None

def open_browser(name):
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
    except Exception as e:
        print("Unexpected error: {}".format(repr(e)))

def visit_url(url):
    try:
        _browser.get(url)
    except Exception as e:
        print("Unexpected error: {}".format(repr(e)))
        
@given("{browser} is installed")
def is_browser_installed_impl(context,browser):
    open_browser(browser.lower())
    visit_url("https://www.google.com")
    return True

@when("I launch {browser}")
def launch_browser_impl(context,browser):
    open_browser(browser.lower())
    
@when("I navigate to {url}")
def navigate_to_url_impl(context,url):
    visit_url(url)
    assert_true(_browser.current_url == url,"Mismatched URLs {}".format(_browser.current_url))

@then("Chrome is open")
def browser_is_open(context):
    assert_true(is_program_running("chrome.exe"), "Browser {} is not running".format("chrome.exe"))
