from selenium import webdriver
from django.contrib.staticfiles.testing import LiveServerTestCase
from django.urls import reverse
from functional_tests.helpers import *
import time


class TestMainPage(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver')
        self.url = 'http://localhost:'
        self.port = 8000
        self.domain = self.url + str(self.port)
        self.login_url = self.domain+reverse('login')
        self.main_page_url = self.domain+reverse('index')

        self.browser.get(self.login_url)
        self.browser.find_element_by_name('username').send_keys('daniel')
        self.browser.find_element_by_name('password').send_keys('testpass')
        self.browser.find_element_by_id('submit-btn').click()

    def tearDown(self):
        self.browser.close()

    def test_login_and_redirect_index(self):
        # the user request the page for the first time
        self.assertEqual(self.browser.current_url, self.main_page_url)

    # This test was designed to add a new word and be sure that it was added correctly.
    def test_add_new_word(self):
        word = get_random_line_from_file(AVAILABLE_WORDS_FILE)
        clean_word = word.strip('\n')
        self.browser.find_element_by_id('word-to-find').send_keys(clean_word)
        self.browser.find_element_by_id("btn-add-new-word").click()
        time.sleep(1)  # wait the creation of yes button
        self.browser.find_element_by_xpath('//button[text()="yes"]').click()
        time.sleep(1)  # wait the creation of close button
        self.browser.find_element_by_xpath('//button[text()="close"]').click()
        self.browser.refresh()
        time.sleep(1)
        self.browser.find_element_by_xpath('//input[@type="search"]').send_keys(clean_word)
        time.sleep(1)
        value_in_table = self.browser.find_element_by_xpath('//a[text()="'+clean_word+'"]').text
        self.assertEqual(clean_word, value_in_table)
        set_word_as_used(word)
        parent = self.browser.find_element_by_xpath('//a[text()="'+clean_word+'"]/parent::td/parent::tr')
        # It ensures the attempts, hits and accuracy attributes are in zero
        self.assertTrue("<td>0</td><td>0</td><td>0.0%</td>" in parent.get_attribute('innerHTML'))

