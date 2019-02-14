from test_assignment.selenium.utils.urls import TWEET_URL


class TweetPage:
    
    follow_button_xpath = "//button[.='Follow']"
    text_xpath = "//*[@name='text']"
    tweet_button_xpath = "//button[.='Tweet']"
    first_tweet_name_xpath = "//div[@class='tweet']/h3"
    tweet_counter_xpath = "//form/p[contains(text(),'Tweet')]"
    displayed_tweet_xpath = "//div[@class='tweet']"

    def __init__(self, browser):
        self.browser = browser

    @property
    def text(self):
        return self.browser.find_element_by_xpath(self.text_xpath)

    @property
    def tweet_button(self):
        return self.browser.find_element_by_xpath(self.tweet_button_xpath)

    @property
    def first_tweet_text(self):
        return self.browser.find_element_by_xpath(self.first_tweet_name_xpath)

    @property
    def follow_button(self):
        return self.browser.find_element_by_xpath(self.follow_button_xpath)

    def get_counter(self):
        counter_element = self.browser.find_element_by_xpath(self.tweet_counter_xpath)
        # gets number from text "Tweet: <number>"
        number = int(counter_element.text.split(" ")[1])
        return number
    
    def get_number_of_displayed_tweets(self):
        return len(self.browser.find_elements_by_xpath(self.displayed_tweet_xpath))

    def visit(self):
        self.browser.get(TWEET_URL)
