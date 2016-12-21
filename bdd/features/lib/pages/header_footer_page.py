from selenium.webdriver.common.by import By
from base_page_object import BasePage
import time
import re

class HeaderFooterPage(BasePage):
    locator_dictionary = {
        #header
        "mainLogo": (By.CLASS_NAME, "navbar-header"),
        "commentCaMarche": (By.XPATH, "//a[@href='/comment_ca_marche']"),
        "tarifs": (By.XPATH, "//a[@href='/tarifs']"),
        "seConnecter": (By.XPATH, "//a[@href='/users/sign_in']"),
        "sinscrire": (By.XPATH, "//a[@href='/users/sign_up']"),
        "proposerMaVoiture": (By.XPATH, "//a[@href='/louer-sa-voiture']"),
        
        #footer blue bar
        #tel
        
        #aide
        
        #en savoir plus
        
        #l'entreprise
        
        
        #footer white bar
        #mentionsLegales
        #cguKoolicar
        #politiqueDeConfidentialite
        #cguMangopay
        
        
    }
    
    def __init__(self, driver):
        BasePage.__init__(
            self,
            driver,
            "https://www.koolicar.com")

    def locator_click(self,locator):
        self.find_element(*self.locator_dictionary[locator]).click()
    
    def main_logo(self):
        self.locator_click("mainLogo")
        time.sleep(2)
        self.logger.debug("url: "+self.get_current_url())
        assert self.match_current_url_with_regex("www.koolicar.com.?$"), "invalid url {}".format(self.get_current_url())
    
    def comment_ca_marche(self):
        self.locator_click("commentCaMarche")
        time.sleep(2)
        self.logger.debug("url: "+self.get_current_url())
        assert self.match_current_url_with_regex("www.koolicar.com.comment_ca_marche.?$"), "invalid url {}".format(self.get_current_url())
    
    def test_can_click_all_header_buttons(self):
        self.locator_click("mainLogo")
        time.sleep(2)
        self.locator_click("commentCaMarche")
        time.sleep(2)
        self.locator_click("tarifs")
        time.sleep(2)
        self.locator_click("seConnecter")
        time.sleep(2)
        self.locator_click("sinscrire")
        time.sleep(2)