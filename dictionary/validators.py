from django.core.exceptions import ValidationError


def is_alphabetical(input_string):
    if not input_string.strip().isalpha():
        raise ValidationError('Only characters allowed')
