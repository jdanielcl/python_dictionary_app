from django.test import TestCase
from dictionary.models import Word, Attempts
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.contrib.auth.models import User


class TestModels(TestCase):

    def setUp(self):
        self.right_name = 'flatter'
        self.wrong_name = 'flatter 23'
        self.word = Word.objects.create(name=self.right_name)
        self.user = User.objects.create_user(username='test',email=None,password='testing')

    def test_word_is_alphabet_only(self):
        self.assertEqual(self.word.name, self.right_name)

    def test_word_is_not_alphabet(self):
        try:
            word_fail = Word.objects.create(name=self.wrong_name)
            self.assertNotEqual(word_fail.name, self.wrong_name)
        except ValidationError:
            self.assertRaises(ValidationError)

    def test_word_is_unique(self):
        try:
            word_fail = Word.objects.create(name=self.right_name)
            self.assertNotEqual(word_fail.name, self.right_name)
        except IntegrityError:
            self.assertRaises(IntegrityError)

    def test_attempt_creation(self):
        attempt = Attempts.objects.create(user=self.user, word=self.word)
        self.assertEqual(attempt.attempts, 0)
        self.assertEqual(attempt.hits, 0)
        self.assertEqual(attempt.accuracy, 0)

    def test_attempt_accuracy(self):
        attempt_one = Attempts.objects.create(user=self.user, word=self.word, attempts=8, hits=3)
        attempt_two = Attempts.objects.create(user=self.user, word=self.word, attempts=28, hits=14)
        self.assertEqual(attempt_one.accuracy, 37.5)
        self.assertEqual(attempt_two.accuracy, 50.0)

