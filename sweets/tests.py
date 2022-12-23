from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from django.contrib.auth.models import User

class GeneralTestCase(TestCase):
    testing_url = 'http://localhost:8000/'

    def setUp(self):
        """
        Sets up the webpage - be sure to have server running
        """
        self.browser = webdriver.Firefox()
        self.browser.get(self.testing_url)

    
    def test_there_are_sweets(self):
        """
        Checks to see if all of the sweets appear 

        In order for it to work, all but one must be commentted - create 7 different tests

        """
        #self.assertIn ('Fruit BonBons',self.browser.page_source)
        #self.assertIn ('Everton Mints',self.browser.page_source)
        self.assertIn ('Aniseed Twists',self.browser.page_source)
        # self.assertIn ('Chocolate Limes',self.browser.page_source)
        # self.assertIn ('Pear Drops',self.browser.page_source)
        # self.assertIn ('Kola Kubes',self.browser.page_source)
        # self.assertIn ('Rhubard & Custard',self.browser.page_source)

    def tearDown(self):
        """
        Shuts down the browser
        """
        self.browser.quit()