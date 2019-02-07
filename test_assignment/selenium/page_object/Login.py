from test_assignment.selenium.utils.urls import LOGIN_URL

class Login():
	
	username_xpath = "//*[@name='username']"
	password_xpath = "//*[@name='password']"
	login_xpath = "//button[.='Login']"


	def __init__(self, browser):
		self.browser = browser


	@property
	def username(self):
		username_field = self.browser.find_element_by_xpath(self.username_xpath)
		return username_field

	@property
	def password(self):
		password_field = self.browser.find_element_by_xpath(self.password_xpath)
		return password_field

	@property
	def login_button(self):
		login_button = self.browser.find_element_by_xpath(self.login_xpath)
		return login_button

	def visit(self):
		self.browser.get(LOGIN_URL)
