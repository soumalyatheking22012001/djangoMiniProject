from django.test import TestCase,LiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .models import UserFile
from .views import edit_email
from .forms import emailForm


def create_user():
	user = UserFile(name="SU",first_name="Yu",password="234",email_address="yu@gmail.com")
	user.save()
	return user

class UserFileTests(TestCase):
	def test_emailForm(self):
		form_data = {'email_address':'yyy@gmail.com'}
		form = emailForm(data=form_data)
		self.assertTrue(form.is_valid())

class editEmailTestCase(LiveServerTestCase):

	def setUp(self):
		self.selenium = webdriver.Chrome(executable_path='G:/projects/chromedriver.exe')
		super(editEmailTestCase,self).setUp()

	def tearDown(self):
		self.selenium.quit()
		super(editEmailTestCase,self).tearDown()

	def test_edit_email(self):
		selenium = self.selenium
		user = create_user()
		selenium.get('http://127.0.0.1:8000/account/profile/1')

		# find form elements
		edit  = selenium.find_element_by_id('edit')
		edit.click()
		email_address = selenium.find_element_by_id('email_edit_form')

		submit = selenium.find_element_by_name('save')

		# fill the form
		wait = new WebDriverWait(selenium,10)
		email_address = wai.until(EC.visibility_of_element_located)
		email_address.send_keys('rrr@gmail.com')

		# submit the form
		submit.send_keys(Keys.RETURN)

		selenium.assertIn('rrr@gmail.com',selenium.page_source)


# Create your tests here.
