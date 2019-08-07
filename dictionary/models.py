from django.db import models
from django.core.exceptions import ValidationError
from dictionary.validators import is_alphabetical


class Word(models.Model):
    name = models.CharField(max_length=40, validators=[is_alphabetical, ])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        is_alphabetical(self.name)
        super(Word, self).save(*args, **kwargs)
