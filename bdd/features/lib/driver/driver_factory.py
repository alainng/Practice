from selenium.common.exceptions import WebDriverException
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
                return webdriver.Firefox(executable_path=r"C:\selenium_drivers\geckodriver.exe")          
            else:
                return webdriver.Chrome(executable_path=r"C:\selenium_drivers\chromedriver.exe")
        except WebDriverException as wde:
            print("{} did not open as expected".format(wde))
            raise
        except Exception as e:
            print("Unexpected error: {}".format(repr(e)))