from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from dictionary.models import Word, Attempts
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='user', password='pass')
        self.user_no_owner = User.objects.create_user(username='user_no_owner', password='pass')
        self.client.login(username='user', password='pass')

        self.list_url = reverse('words-list')
        self.word_detail_url = reverse('words-detail', args={1})
        self.list_attempts_url = reverse('attempts-list')
        self.detail_attempts_url = reverse('attempts-detail', args={1})
        self.detail_attempts_no_owner_url = reverse('attempts-detail', args={2})

        self.word = Word.objects.create(id=1, name='flatter')
        self.attempt_owner = Attempts.objects.create(user=self.user, word=self.word)
        self.attempt_no_owner = Attempts.objects.create(user=self.user_no_owner, word=self.word)

        self.content_type = 'application/json'

    def test_view_word_list_ok(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)

    def test_view_word_detail_ok(self):
        response = self.client.get(self.word_detail_url)
        self.assertEqual(response.status_code, 200)

    def test_view_attempt_list_ok(self):
        response = self.client.get(self.list_attempts_url)
        self.assertEqual(response.status_code, 200)

    def test_view_attempt_detail_ok(self):
        response = self.client.get(self.detail_attempts_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.__getitem__('word'), self.word.id)

    def test_view_attempt_detail_not_owner(self):
        response = self.client.get(self.detail_attempts_no_owner_url)
        self.assertEqual(response.status_code, 404)

    def test_view_attempt_successful_update(self):
        data = json.dumps({'word': 1, 'attempts': 0, 'hits': 0, 'success': True})
        response = self.client.put(self.detail_attempts_url, data=data, content_type=self.content_type)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.__getitem__('attempts'), 1)
        self.assertEqual(response.data.__getitem__('hits'), 1)

    def test_view_attempt_update_not_owner(self):
        data = json.dumps({'word': 1, 'attempts': 0, 'hits': 0, 'success': True})
        response = self.client.put(self.detail_attempts_no_owner_url, data=data, content_type=self.content_type)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(self.attempt_no_owner.attempts, 0)
        self.assertEqual(self.attempt_no_owner.hits, 0)

    def test_view_attempt_not_successful_update(self):
        data = json.dumps({'word': 1, 'attempts': 0, 'hits': 0, 'success': False})
        response = self.client.put(self.detail_attempts_url, data=data, content_type=self.content_type)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.__getitem__('attempts'), 1)
        self.assertEqual(response.data.__getitem__('hits'), 0)

    def test_view_attempt_bad_request(self):
        data = json.dumps({'word': 1, 'attempts': 0, 'hits': 0})
        response = self.client.put(self.detail_attempts_url, data=data, content_type=self.content_type)
        self.assertEqual(response.status_code, 400)

    def test_view_attempt_post_not_allowed(self):
        data = json.dumps({'word': 1, 'user': 1, 'attempts': 0, 'hits': 0})
        response = self.client.post(self.detail_attempts_url, data=data, content_type=self.content_type)
        self.assertEqual(response.status_code, 405)

    def test_view_attempt_delete_not_allowed(self):
        response = self.client.delete(self.detail_attempts_url)
        self.assertEqual(response.status_code, 405)

    def test_view_word_update_not_allowed(self):
        data = json.dumps({'id': 1, 'name': 'flatter'})
        response = self.client.put(self.word_detail_url, data=data, content_type=self.content_type)
        self.assertEqual(response.status_code, 405)

    def test_view_word_delete_not_allowed(self):
        response = self.client.delete(self.word_detail_url)
        self.assertEqual(response.status_code, 405)

