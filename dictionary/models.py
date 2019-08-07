from django.db import models
from django.core.exceptions import ValidationError
from dictionary.validators import has_numbers


class Word(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        try:
            has_numbers(self.name)
            super(Word, self).save(*args, **kwargs)
        except ValidationError:
            pass

