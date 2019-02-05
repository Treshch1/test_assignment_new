class TweetPage(object):


	follow_button_xpath = "//button[.='Follow']"
	text_xpath = "//*[@name='text']"
	tweet_xpath = "//button[@type='submit']"
	first_tweet_name_xpath = "//div[@class='tweet']/h3"


	def __init__(self, browser):
		self.browser = browser


	def Text(self, text):
		text_field = self.browser.find_element_by_xpath(self.text_xpath)
		text_field.clear()
		text_field.send_keys(text)

	def Tweet(self):
		tweet_button = self.browser.find_element_by_xpath(self.tweet_xpath)
		tweet_button.click()

	def FirstTweetText(self):
		first_tweet_name = self.browser.find_element_by_xpath(self.first_tweet_name_xpath)
		return first_tweet_name.text
