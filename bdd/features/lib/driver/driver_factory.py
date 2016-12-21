from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver

class DriverFactory:
    def create_driver(self,input_name):    
        name=input_name.lower()
        try:
            if name == "ie":
                return webdriver.Ie(executable_path=r"C:\selenium_drivers\IEDriverServer.exe")
            elif name == "edge":
                return webdriver.Edge(executable_path=r"C:\selenium_drivers\MicrosoftWebDriver.exe")
            elif name == "safari":
                return webdriver.Safari()
            elif name == "firefox":  
                binary=FirefoxBinary(r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe")
                return webdriver.Firefox(executable_path=r"C:\selenium_drivers\geckodriver.exe",firefox_binary=binary)      
            else:
                #deal with uncertain certs http://stackoverflow.com/questions/24507078/how-to-deal-with-certificates-using-selenium
                options=webdriver.ChromeOptions()
                options.add_argument('--ignore-certificate-errors')
                return webdriver.Chrome(executable_path=r"C:\selenium_drivers\chromedriver.exe",chrome_options=options)
        except WebDriverException as wde:
            #"Make sure your drivers are of the right bitness"
            print("{} did not open as expected".format(wde))
            raise
        except Exception as e:
            print("Unexpected error: {}".format(repr(e)))
