from django.db import models
from dictionary.validators import is_alphabetical


class Word(models.Model):
    name = models.CharField(max_length=40, unique=True, validators=[is_alphabetical, ])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        is_alphabetical(self.name)
        super(Word, self).save(*args, **kwargs)
