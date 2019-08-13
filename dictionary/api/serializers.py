from abc import ABC

from rest_framework import serializers
from dictionary.models import Word, Attempts


class WordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Word
        fields = ('id', 'name')


class AttemptsSerializer(serializers.ModelSerializer):
    word_name = serializers.SerializerMethodField()

    class Meta:
        model = Attempts
        fields = ('word', 'added_date', 'attempts', 'hits', 'word_name', 'accuracy')

    def get_word_name(self, obj):
        return obj.word.name