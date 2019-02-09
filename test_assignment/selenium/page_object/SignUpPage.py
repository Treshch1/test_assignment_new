from test_assignment.selenium.utils.urls import SIGNUP_URL


class SignUpPage:

    email_xpath = "//*[@name='email']"
    password_1_xpath = "//*[@name='password1']"
    password_2_xpath = "//*[@name='password2']"
    signup_button_xpath = "//button[.='Sign up']"

    def __init__(self, browser):
        self.browser = browser

    @property
    def email(self):
        return self.browser.find_element_by_xpath(self.email_xpath)

    @property
    def password1(self):
        return self.browser.find_element_by_xpath(self.password_1_xpath)
    
    @property
    def password2(self):
        return self.browser.find_element_by_xpath(self.password_2_xpath)
    
    @property
    def signup_button(self):
        return self.browser.find_element_by_xpath(self.signup_button_xpath)

    def visit(self):
        self.browser.get(SIGNUP_URL)
