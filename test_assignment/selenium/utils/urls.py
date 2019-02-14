from django.urls import reverse
from urllib.parse import urljoin


BASE_URL = 'http://localhost:8080/'

TWEET_URL = urljoin(BASE_URL, reverse('home'))

LOGIN_URL = urljoin(BASE_URL, reverse('login'))

SIGNUP_URL = urljoin(BASE_URL, reverse('signup')) 
