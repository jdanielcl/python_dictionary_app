from rest_framework import viewsets
from dictionary.models import Word
from dictionary.api.serializers import WordSerializer


class WordViewSet(viewsets.ModelViewSet):

    queryset = Word.objects.all()
    serializer_class = WordSerializer
