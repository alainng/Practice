from selenium.webdriver.common.by import By
from base_page_object import BasePage
import time
import re

class HeaderFooterPage(BasePage):
    locator_dictionary = {
        "mainLogo": (By.CLASS_NAME, "navbar-header"),
        "commentCaMarche": (By.XPATH, "//a[@href='/comment_ca_marche']"),
        "tarifs": (By.XPATH, "//a[@href='/tarifs']"),
        "seConnecter": (By.XPATH, "//a[@href='/users/sign_in']"),
        "sinscrire": (By.XPATH, "//a[@href='/users/sign_up']"),
        "proposerMaVoiture": (By.XPATH, "//a[@href='/louer-sa-voiture']"),
        
    }
    
    def __init__(self, driver):
        BasePage.__init__(
            self,
            driver,
            "https://www.koolicar.com")

    def click_locator(self,locator):
        self.find_element(*self.locator_dictionary[locator]).click()
    
    def test_header(self):
        self.click_locator("mainLogo")
        time.sleep(2)
        self.click_locator("commentCaMarche")
        time.sleep(2)
        self.click_locator("tarifs")
        time.sleep(2)
        self.click_locator("seConnecter")
        time.sleep(2)
        self.click_locator("sinscrire")
        time.sleep(2)