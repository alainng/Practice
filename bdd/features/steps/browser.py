from behave import *
from selenium import webdriver
from nose.tools import assert_raises, assert_true, assert_false


@given("Chrome is installed")
def is_chrome_installed(context):
    return True

@when("I launch Chrome")
def launch_browser(context):
    return True
    

@then("Chrome is open")
def browser_is_open(context):
    return True
