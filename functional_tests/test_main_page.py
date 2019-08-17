from selenium import webdriver
from django.contrib.staticfiles.testing import LiveServerTestCase
from django.urls import reverse
from django.contrib.auth.models import User
import time


class TestMainPage(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver')
        self.url = 'http://localhost:'
        self.port = 8000
        self.domain = self.url + str(self.port)
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        self.user = User.objects.create_user(**self.credentials)

    def tearDown(self):
        self.browser.close()

    def test_login_fields_working(self):
        login_url = self.domain + reverse('login')

        print(self.user)
        # the user request the page for the first time
        self.browser.get(login_url)
        self.browser.find_element_by_name('username').send_keys(self.credentials.get('username'))
        self.browser.find_element_by_name('password').send_keys(self.credentials.get('password'))
        self.browser.find_element_by_id('submit-btn').click()
        time.sleep(10)
