import pytest
from model_mommy import mommy
from selenium.webdriver import Firefox, FirefoxOptions
from django.conf import get_user_model


User = get_user_model()


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
	user.set_password('test1234')
	user.save()
	return user
