from django.core.exceptions import ValidationError


def is_alphabetical(input_string):
    preprocessed_input = input_string.replace(' ', '').replace('-', '')
    if not preprocessed_input.isalpha():
        raise ValidationError('Only characters allowed')
