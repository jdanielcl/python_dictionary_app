from django import forms
from dictionary.validators import is_alphabetical


class WordForm(forms.Form):
    name = forms.CharField(validators=[is_alphabetical, ])
