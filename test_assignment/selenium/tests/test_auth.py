from test_assignment.selenium.page_object.LoginPage import LoginPage
from test_assignment.selenium.page_object.SignUpPage import SignUpPage
from test_assignment.selenium.page_object.TweetPage import TweetPage
from test_assignment.apps.account.models import User


def test_login(browser, user):
    
    login_page = LoginPage(browser)
    tweet_page = TweetPage(browser)
    user = user()

    login_page.visit()

    login_page.username.send_keys(user.email) 
    login_page.password.send_keys('1qaz2wsx0')
    login_page.login_button.click()

    assert tweet_page.tweet_button.is_displayed()


def test_signup(browser):

    signup_page = SignUpPage(browser)
    tweet_page = TweetPage(browser)
    test_password = '1qaz2wsx0'

    signup_page.visit()

    assert User.objects.count() == 0
    signup_page.email.send_keys('vladislavtreshcheyko@gmail.com')
    signup_page.password1.send_keys(test_password)
    signup_page.password2.send_keys(test_password)
    signup_page.signup_button.click()
    assert User.objects.count() == 1
    assert tweet_page.tweet_button.is_displayed()
