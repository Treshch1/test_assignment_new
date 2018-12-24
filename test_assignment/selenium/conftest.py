import pytest
from selenium.webdriver import Firefox, FirefoxOptions


@pytest.fixture(scope='session')
def browser(live_server):
    """ A browser instance which closes after the testrun. """
    options = FirefoxOptions()
    options.add_argument('headless')

    browser_ = Firefox(options=options)

    yield browser_

    browser_.quit()
