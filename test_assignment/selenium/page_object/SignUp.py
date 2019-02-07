from test_assignment.selenium.utils.urls import SIGNUP_URL

class SignUp():

	email_xpath = "//*[@name='email']"
	password_1_xpath = "//*[@name='password1']"
	password_2_xpath = "//*[@name='password2']"
	signup_button_xpath = "//button[.='Sign up']"


	def __init__(self, browser):
		self.browser = browser

	@property
	def email(self):
		email_field = self.browser.find_element_by_xpath(self.email_xpath)
		return email_field

	@property
	def password1(self):
		password_1_field = self.browser.find_element_by_xpath(self.password_1_xpath)
		return password_1_field
	
	@property
	def password2(self):
		password_2_field = self.browser.find_element_by_xpath(self.password_2_xpath)
		return password_2_field
	
	@property
	def signup_button(self):
		signup_button = self.browser.find_element_by_xpath(self.signup_button_xpath)
		return signup_button

	def visit(self):
		self.browser.get(SIGNUP_URL)
