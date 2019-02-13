import pytest
from model_mommy import mommy
from selenium.webdriver import Firefox, FirefoxOptions
from test_assignment.apps.account.models import User
from test_assignment.apps.tweet.models import Tweet
from test_assignment.selenium.page_object.LoginPage import LoginPage
from faker import Faker


fake = Faker()

@pytest.fixture(scope='function')
def browser(live_server):
    """ A browser instance which closes after the testrun. """
    options = FirefoxOptions()
    options.add_argument('headless')

    browser_ = Firefox(options=options)
    
    yield browser_

    browser_.quit()


@pytest.fixture
def user(user_factory):
    user = user_factory()
    return user


@pytest.fixture
def user_factory(db):
    def _user(**kwargs):
        user_kwargs = {"email": fake.safe_email}
        user_kwargs.update(kwargs)
        password = user_kwargs.pop('password', '1qaz2wsx0')
        created_user = mommy.make(User, **user_kwargs)
        created_user.set_password(password)
        created_user.save()
        return created_user
    return _user


@pytest.fixture
def tweet_factory(db):
    def _tweet(**kwargs):
        tweet_kwargs = {"text": fake.text()}
        tweet_kwargs.update(kwargs)
        created_tweet = mommy.make(Tweet, **tweet_kwargs)
        created_tweet.save()
        return created_tweet
    return _tweet


@pytest.fixture
def authorized_user(browser, user_factory):
    user = user_factory()
    login_page = LoginPage(browser)
    login_page.visit()
    login_page.username.send_keys(user.email)
    login_page.password.send_keys('1qaz2wsx0')
    login_page.login_button.click()
    return user


@pytest.fixture
def user_with_tweet(user_factory, tweet_factory):
    user = user_factory()
    tweet = tweet_factory(user=user)
