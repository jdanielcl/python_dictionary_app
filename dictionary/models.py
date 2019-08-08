from django.db import models
from dictionary.validators import is_alphabetical
from django.contrib.auth.models import User


class Word(models.Model):
    name = models.CharField(max_length=40, unique=True, validators=[is_alphabetical, ])
    users = models.ManyToManyField(User, through='Attempts')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        is_alphabetical(self.name)
        super(Word, self).save(*args, **kwargs)


class Attempts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)
    attempts = models.IntegerField(default='0')
    hits = models.IntegerField(default=0)

    @property
    def accuracy(self):
        try:
            accuracy = self.hits*100/self.attempts
        except ZeroDivisionError:
            accuracy = 0
        return accuracy

