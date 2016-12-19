from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver

class DriverFactory:
    def getDriver(self,input_name):    
        name=input_name.lower()
        try:
            if name == "ie":
                return webdriver.Ie(executable_path=r"C:\selenium_drivers\IEDriverServer.exe")
            elif name == "edge":
                return webdriver.Edge(executable_path=r"C:\selenium_drivers\MicrosoftWebDriver.exe")
            elif name == "firefox":  
                binary=FirefoxBinary(r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe")
                return webdriver.Firefox(executable_path=r"C:\selenium_drivers\geckodriver.exe",firefox_binary=binary)      
            else:
                return webdriver.Chrome(executable_path=r"C:\selenium_drivers\chromedriver.exe")
        except WebDriverException as wde:
            #"Make sure your drivers are of the right bitness"
            print("{} did not open as expected".format(wde))
            raise
        except Exception as e:
            print("Unexpected error: {}".format(repr(e)))
