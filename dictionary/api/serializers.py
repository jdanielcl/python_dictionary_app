from abc import ABC

from rest_framework import serializers
from dictionary.models import Word


class WordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Word
        fields = ('id', 'name')
