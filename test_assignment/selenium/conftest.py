import pytest
from model_mommy import mommy
from selenium.webdriver import Firefox, FirefoxOptions
from test_assignment.apps.account.models import User
from test_assignment.selenium.page_object.LoginPage import LoginPage


@pytest.fixture(scope='function')
def browser(live_server):
    """ A browser instance which closes after the testrun. """
    options = FirefoxOptions()
    options.add_argument('headless')

    browser_ = Firefox(options=options)
    
    yield browser_

    browser_.quit()


@pytest.fixture
def user(db):
    def _user(**kwargs):
        user_kwargs = {'email': 'email@example.com'}
        user_kwargs.update(kwargs)
        password = user_kwargs.pop('password', '1qaz2wsx0')
        created_user = mommy.make(User, **user_kwargs)
        created_user.set_password(password)
        created_user.save()
        return created_user
    return _user


@pytest.fixture
def authorized_user(browser, user):
    user = user()
    login_page = LoginPage(browser)
    login_page.visit()
    login_page.username.send_keys(user.email)
    login_page.password.send_keys('1qaz2wsx0')
    login_page.login_button.click()
