class Login(object):
	
	username_xpath = "//*[@name='username']"
	password_xpath = "//*[@name='password']"
	login_xpath = "//button[@type='submit']"
	warning_xpath = "//li"


	def __init__(self, browser):
		self.browser = browser


	def Username(self, username):
		username_field = self.browser.find_element_by_xpath(self.username_xpath)
		username_field.clear()
		username_field.send_keys(username)

	def Password(self, password):
		password_field = self.browser.find_element_by_xpath(self.password_xpath)
		password_field.clear()
		password_field.send_keys(password)

	def LogIn(self):
		login_button = self.browser.find_element_by_xpath(self.login_xpath)
		login_button.click()

	def Warning(self):
		warning = self.browser.find_element_by_xpath(self.warning_xpath)
		return warning.text