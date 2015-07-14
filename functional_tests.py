from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		#Alice hear about our to-do list website
		#She opens our website
		self.browser.get('http://localhost:8000')

		#She notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		#She is invited to enter a to-do item straight away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)

		# Alice types "buy feta cheess" into a text box
		inputbox.send_keys('buy feta cheese')

		# Alice hits enter, the page updates and it shows "buy feta cheese" 
		# in her to-do list
		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: buy feta cheese' for row in rows)
		)

		# Alice can see that there's still a text box and she enters "buy meat"
		set.fail('Finish the test!')

# The page updates again, and now shows both items on her list

# Alice wonders if the site will remember her list. Then she sees 
# that the site has generated a unique URL for her -- there is 
# some explanatory text to that effect.

# She visits that URL - her to-do list is still there.

# Satisfied, she goes on with her day

if __name__ == '__main__':
	unittest.main(warnings='ignore')