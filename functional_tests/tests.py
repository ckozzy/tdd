from django.test import LiveServerTestCase
from selenium import webdriver
#import unittest
from selenium.webdriver.common.keys import Keys


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
     # Edith has heard about a cool new online to-do app. She goes 
     # to check out its homepage
     self.browser.get(self.live_server_url)
     
     # She notices the page title and header mention to-do lists
     self.assertIn('To-Do', self.browser.title)
     header_text = self.browser.find_element_by_tag_name('h1').text
     self.assertIn('To-Do', header_text)
     
     # She is invited to enter a to-do item straight away
     inputbox = self.browser.find_element_by_id('id_new_item')
     self.assertEqual(
	      inputbox.get_attribute('placeholder'),
	      'Enter a to-do item'
      )
     
     
      # She types "Buy peacock feathers" into a test box
     inputbox.send_keys('Buy peacock feathers')
      
      # When she hits enter, she is taken to a new URL, and now the page lists
      # "1: Buy peacock feathers" as an item in a to-do list table
     inputbox.send_keys(Keys.ENTER)
     edith_list_url = self.browser.current_url
     import time
     time.sleep(10)
     self.assertRegex(edith_list_url, '/lists/.+')
     """ failing above will not work till nd chapter 6"""

     self.check_for_row_in_list_table('1: Buy peacock feathers')

     
     # There is still a text box inviting her to add another item. She
     # enters "Use peacock feathers to make a fly"
     inputbox = self.browser.find_element_by_id('id_new_item')
     inputbox.send_keys('Use peacock feathers to make a fly')
     inputbox.send_keys(Keys.ENTER)
     

     
     # The page updtes again, and now shows both items on her list
     self.check_for_row_in_list_table('1: Buy peacock feathers')
     self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
     
     # Edith wonders if the siet will remember her list.  Then she sees 
     # that the site has generated a unique URL for her -- ther is some 
     # eplanatory text to that effect.
     self.fail('Finish the test!')
     
     # Se visits that URL - her to-do list is still there.
     
     
     
    


