from django.test import LiveServerTestCase
from selenium import webdriver
#import unittest
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTest(LiveServerTestCase):
  
  def setUp(self):
    self.browser = webdriver.Firefox()
    self.browser.implicitly_wait(3)
    
  def tearDown(self):
    self.browser.quit()
  
  def check_for_row_in_list_table(self, row_text):
     table = self.browser.find_element_by_id('id_list_table')
     rows = table.find_elements_by_tag_name('tr')     
     self.assertIn(row_text, [row.text for row in rows])
     
  def test_can_start_a_list_and_retrieve_it_later(self):
    # ozzy decides he wants to back into css bootstrap slowly so he begins by 
    # slowly adding the various aspects of bootstrp
    
    # first he open up a browser to the home page 
    self.browser.get(self.live_server_url)
    
    time.sleep(20)
    
    # ozzy decided to copy a test in to see if it got rid of an error
    edith_list_url = self.browser.current_url
    self.assertRegex(edith_list_url, 'localhost:8081')

     
    
    # he verifies that the header is using the header from bootstrap with little modificatins
    
    
    # and entere
    
#    self.browser.quit()
     
     
     
     
     