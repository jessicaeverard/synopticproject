from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from django.contrib.auth.models import User
import time

class GeneralTestCase(TestCase):
    testing_url = 'http://localhost:8000/'

    def setUp(self):
        """
        Sets up the webpage - be sure to have server running
        """
        self.browser = webdriver.Firefox()
        self.browser.get(self.testing_url)

    
    # def test_there_are_sweets(self):
    #     """
    #     Checks to see if all of the sweets appear 

    #     In order for it to work, all but one must be commentted - create 7 different tests

    #     """
    #     #self.assertIn ('Fruit BonBons',self.browser.page_source)
    #     #self.assertIn ('Everton Mints',self.browser.page_source)
    #     self.assertIn ('Aniseed Twists',self.browser.page_source)
    #     # self.assertIn ('Chocolate Limes',self.browser.page_source)
    #     # self.assertIn ('Pear Drops',self.browser.page_source)
    #     # self.assertIn ('Kola Kubes',self.browser.page_source)
    #     # self.assertIn ('Rhubard & Custard',self.browser.page_source)

    def test_add_to_cart(self):
        """
        Test to see if a user can add item to cart and that it appears on the cart details page.
        
        """
        quantity = self.browser.find_element('css selector','textarea')
        quantity.send_keys('10')
        self.browser.find_element('xpath', "//button[contains(., 'Add to cart')]").click()
        self.browser.find_element('xpath', "//a[contains(., 'Go To Cart')]").click()
        self.browser.find_element('xpath', "//p[contains(., 'name Rhubard & Custard')]")
        self.assertIn ('10',self.browser.page_source)

    def test_delete_item_from_cart(self):
        """
        Test to see if the item is deleted from the cart

        Does depend on the add to cart test as there needs to be an item in the cart.
        """
        self.browser.find_element('xpath', "//a[contains(., 'Go To Cart')]").click()
        self.browser.find_element('xpath', "//a[contains(., 'Delete')]").click()
        try:
            self.browser.find_element('xpath', "//p[contains(., 'name Rhubard & Custard')]")
        except NoSuchElementException:
            return False
        return True

    def tearDown(self):
        """
        Shuts down the browser
        """
        self.browser.quit()