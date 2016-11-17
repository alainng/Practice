from behave import *
from selenium import webdriver
from nose.tools import assert_raises, assert_true, assert_false
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from system import is_program_running
import settings

_browser = None

def is_64bit():
    try:
        os.environ["PROGRAMFILES(X86)"]
        bits = 64
        return True
    except:
        bits = 32
        return False

def get_firefox_default_binary_location():
    if is_64bit():
        return 'C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'
    else:
        return 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'

def get_firefox_version():
    version=subprocess.check_output(get_firefox_default_binary_location()+' -v')
    assert_false(version=='',"version is empty {}".format(version))
    print('firefox version{}'.format(version[16:18]))
    return int(version[16:18])

def launch_browser(name):
    global _browser
    try:
        if name == "firefox":            
#             if get_firefox_version()>=48:
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

@then("{} is open")
def browser_is_open(context,browser):
    browser_binary_name=settings.get_binary_name(browser)
    assert_true(is_program_running(browser_binary_name), "Browser {} is not running".format(browser_binary_name))

#Static steps below