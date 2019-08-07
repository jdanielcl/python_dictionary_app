from django.test import TestCase
from dictionary.models import Word
from django.core.exceptions import ValidationError


class TestModels(TestCase):

    def test_word_is_alphabet_only(self):
        word = Word.objects.create(name='flatter')
        self.assertEqual(word.name, 'flatter')

    def test_word_is_not_alphabet(self):
        try:
            word = Word.objects.create(name='flatter1')
        except ValidationError:
            self.assertRaises(ValidationError)
