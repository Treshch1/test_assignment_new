from test_assignment.selenium.page_object.TweetPage import TweetPage
from test_assignment.apps.tweet.models import Tweet


def test_tweet_successful_creation(browser, authorized_user):
    
    tweet_page = TweetPage(browser)
    tweet_text = 'Tweet text'
    
    assert Tweet.objects.count() == 0
    tweet_page.text.send_keys(tweet_text)
    tweet_page.tweet_button.click()
    assert Tweet.objects.count() == 1
    assert tweet_page.first_tweet_text.text == tweet_text    
