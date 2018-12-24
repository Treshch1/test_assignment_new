from test_assignment.selenium.utils.urls import TWEET_URL


def test_tweet_page(browser):
    browser.get(TWEET_URL)
