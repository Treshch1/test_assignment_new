import pytest
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


def test_tweet_following(browser, user_with_tweet, authorized_user):

    tweet_page = TweetPage(browser)

    assert authorized_user.following.count() == 0
    assert tweet_page.get_number_of_displayed_tweets() == 0
    tweet_page.follow_button.click()
    assert authorized_user.following.count() == 1
    assert authorized_user.tweets_counter == 0
    assert tweet_page.get_number_of_displayed_tweets() == 1


@pytest.mark.xfail(reason='Bug with tweets count')
@pytest.mark.parametrize('tweets_quantity', [(0), (1), (15)])
def test_tweet_counting(browser, authorized_user, tweet_factory, tweets_quantity):

    tweet_page = TweetPage(browser)

    assert authorized_user.tweets_counter == 0
    for i in range(tweets_quantity):
        tweet_entity = tweet_factory(user=authorized_user)
    authorized_user.refresh_from_db()
    assert authorized_user.tweets_counter == tweets_quantity
    browser.refresh()
    assert tweet_page.get_counter() == tweets_quantity
    assert tweet_page.get_number_of_displayed_tweets() == tweets_quantity
