from test_assignment.selenium.utils.urls import TWEET_URL


class TweetPage:
    
    follow_button_xpath = "//button[.='Follow']"
    text_xpath = "//*[@name='text']"
    tweet_xpath = "//button[.='Tweet']"
    first_tweet_name_xpath = "//div[@class='tweet']/h3"

    def __init__(self, browser):
        self.browser = browser

    @property
    def text(self):
        return self.browser.find_element_by_xpath(self.text_xpath)

    @property
    def tweet_button(self):
        return self.browser.find_element_by_xpath(self.tweet_xpath)

    @property
    def first_tweet_text(self):
        return self.browser.find_element_by_xpath(self.first_tweet_name_xpath)

    def visit(self):
        self.browser.get(TWEET_URL)
