from django.test import TestCase
from dictionary.models import Word
from dictionary.validators import is_alphabetical
from dictionary.forms import WordForm


class TestForms(TestCase):

    def test_word_form_is_alphabetical_with_space(self):
        word_form = WordForm(
            data={
                'name': 'self confidence',
            }
        )
        self.assertTrue(word_form.is_valid())

    def test_word_form_is_alphabetical_with_score(self):
        word_form = WordForm(
            data={
                'name': 'self-confidence',
            }
        )
        self.assertTrue(word_form.is_valid())

    def test_word_form_is_not_alphabetical(self):
        word_form = WordForm(
            data={
                'name': 'flatter123',
            }
        )
        self.assertFalse(word_form.is_valid())

    def test_word_form_has_data(self):
        word_form = WordForm(
            data={}
        )
        self.assertFalse(word_form.is_valid())
