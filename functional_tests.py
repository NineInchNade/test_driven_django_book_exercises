from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicit_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		#Alice hear about our to-do list website
		#She opens our website
		self.browser.get('http://localhost:8000')

		#She notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

		#She is invited to enter a to-do item straight away
		#[...rest of comments as before]

# Alice types "buy feta chees" into a text box

# Alice hits enter, the page updates and it shows "buy feta cheese" 
# in her to-do list

# Alice can see that there's still a text box and she enters "buy meat"

# The page updates again, and now shows both items on her list

# Alice wonders if the site will remember her list. Then she sees 
# that the site has generated a unique URL for her -- there is 
# some explanatory text to that effect.

# She visits that URL - her to-do list is still there.

# Satisfied, she goes on with her day

if __name__ == '__main__':
	unittest.main(warnings='ignore')