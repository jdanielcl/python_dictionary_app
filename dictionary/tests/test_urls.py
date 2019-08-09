from django.urls import resolve, reverse
from django.test import TestCase
from dictionary.api.viewsets import WordViewSet, AttemptsViewSet


class TestUlrs(TestCase):

    def test_word_list_url(self):
        url = reverse('words-list')
        self.assertEqual(resolve(url).func.cls, WordViewSet)

    def test_word_detail_url(self):
        url = reverse('words-detail', args={'1'})
        self.assertEqual(resolve(url).func.cls, WordViewSet)

    def test_attempt_list(self):
        url = reverse('attempts-list')
        self.assertEqual(resolve(url).func.cls, AttemptsViewSet)