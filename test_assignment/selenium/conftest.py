import pytest
from model_mommy import mommy
from selenium.webdriver import Firefox, FirefoxOptions
from test_assignment.apps.account.models import User


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
	user = mommy.make(User, email='example@example.com')
	user.set_password('1qaz2wsx0')
	user.save()
	return user
