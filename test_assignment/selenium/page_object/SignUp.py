class SignUp(object):


	email_xpath = "//*[@name='email']"
	password_1_xpath = "//*[@name='password1']"
	password_2_xpath = "//*[@name='password2']"
	signup_button_xpath = "//button[@type='submit']"


	def __init__(self, browser):
		self.browser = browser

	
	def Email(self, email):
		email_field = self.browser.find_element_by_xpath(self.email_xpath)
		email_field.clear()
		email_field.send_keys(email)

	def Password1(self, password_1):
		password_1_field = self.browser.find_element_by_xpath(self.password_1_xpath)
		password_1_field.clear()
		password_1_field.send_keys(password_1)
	

	def Password2(self, password_2):
		password_2_field = self.browser.find_element_by_xpath(self.password_2_xpath)
		password_2_field.clear()
		password_2_field.send_keys(password_2)
	
	def SignupButton(self):
		signup_button_field = self.browser.find_element_by_xpath(self.signup_button_xpath)
		signup_button_field.click()