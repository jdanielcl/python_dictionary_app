from rest_framework import viewsets, views
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from dictionary.models import Word
from dictionary.api.serializers import WordSerializer
import requests as req
import json


class WordViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class WordSearch(views.APIView):

    def get(self, request):
        word = request.GET.get('word', None)
        word_definition = req.get(f'https://googledictionaryapi.eu-gb.mybluemix.net/?define={word}&lang=en')
        data = json.loads(word_definition.text)
        return Response(data)
