from urllib.parse import urljoin


BASE_URL = 'http://localhost:8080/'

TWEET_URL = urljoin(BASE_URL, '')

LOGIN_URL = urljoin(BASE_URL, 'account/login/')

SIGNUP_URL = urljoin(BASE_URL, 'account/signup/') 
