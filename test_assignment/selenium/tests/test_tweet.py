import pytest
from test_assignment.selenium.utils.urls import TWEET_URL, LOGIN_URL, SIGNUP_URL
from ..page_object.Login import Login
from ..page_object.SignUp import SignUp
from ..page_object.TweetPage import TweetPage


# @pytest.mark.skip(reason='No need')
def test_login(browser):
    
    login_page = Login(browser)

    browser.get(LOGIN_URL)
    
    login_page.Username('vladislavtreshcheyko@gmail.com')
    login_page.Password('1qaz2wsx0')
    login_page.LogIn()

    assert login_page.Warning() == 'Please enter a correct email and password. Note that both fields may be case-sensitive.'


def test_signup(browser):

	signup_page = SignUp(browser)
	tweet_page = TweetPage(browser)
	
	browser.get(SIGNUP_URL)

	signup_page.Email('vladislavtreshcheyko@gmail.com')
	signup_page.Password1('1qaz2wsx0')
	signup_page.Password2('1qaz2wsx0')
	signup_page.SignupButton()
	
	tweet_page.Text("Tweet text")
	tweet_page.Tweet()

	assert tweet_page.FirstTweetText() == "Tweet text"

