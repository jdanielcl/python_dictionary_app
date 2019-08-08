from django.test import TestCase, Client
from dictionary.api.viewsets import WordViewSet
from django.urls import reverse
from dictionary.models import Word


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('words-list')
        self.detail_url = reverse('words-detail', args={1})

    def test_view_list_ok(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        # self.assertTrue(False)

    def test_view_detail_ok(self):
        Word.objects.create(id=1, name='flatter')
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
