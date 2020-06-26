from test_assignment.selenium.utils.urls import LOGIN_URL


class LoginPage:

    username_xpath = "//*[@name='username']"
    password_xpath = "//*[@name='password']"
    login_xpath = "//button[.='Login']"

    def __init__(self, browser):
       self.browser = browser

    @property
    def username(self):
        return self.browser.find_element_by_xpath(self.username_xpath)

    @property
    def password(self):
        return self.browser.find_element_by_xpath(self.password_xpath)

    @property
    def login_button(self):
        return self.browser.find_element_by_xpath(self.login_xpath)

    def visit(self):
        self.browser.get(LOGIN_URL)

    print('To commit')
