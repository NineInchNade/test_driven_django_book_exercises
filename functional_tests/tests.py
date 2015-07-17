from django.test import LiveServerTestCase

from selenium import webdriver
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
		#Alice hear about our to-do list website
		#She opens our website
		self.browser.get(self.live_server_url)

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

		# Alice hits enter, she is taken to a new URL
		# and now the pages lists "1: buy feta cheese" 
		# as an item in a to-do list		
		inputbox.send_keys(Keys.ENTER)
		alice_list_url = self.browser.current_url
		self.assertRegex(alice_list_url, '/lists/.+')
		self.check_for_row_in_list_table('1: buy feta cheese')
		
		# Alice can see that there's still a text box and she enters "buy meat"
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('buy meat')
		inputbox.send_keys(Keys.ENTER)


		# The page updates again, and now shows both items on her list
		self.check_for_row_in_list_table('2: buy meat')
		self.check_for_row_in_list_table('1: buy feta cheese')

		#Now a new user, Cicci, comes along to the site.

		## We use a new browser session to make sure that no information
		## of Alice's is coming throuhg from cookies etc
		self.browser.quit()
		self.browser = webdriver.Firefox()

		# Cicci visits the home page. There is no sign of Alice's list
		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('buy feeto cheese', page_text)
		self.assertNotIn('buy meat', page_text)

		# Cicci starts a new list by entering a new item.
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('buy almond milk')
		inputbox.send_keys(Keys.ENTER)

		# Cicci gets her own unique URL 
		cicci_list_url = self.browser.current_url
		self.assertRegex(cicci_list_url, '/lists/.+')
		self.assertNotEqual(cicci_list_url, alice_list_url)

		# Again, there is not trace of Alice's list
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('buy feta cheese', page_text)
		self.assertIn('buy almond milk', page_text)

	# Satisfied, they both go on with their day