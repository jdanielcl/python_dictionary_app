from django.core.exceptions import ValidationError


def has_numbers(input_string):
    if any(char.isdigit() for char in input_string):
        raise ValidationError('The input data contains numbers')
