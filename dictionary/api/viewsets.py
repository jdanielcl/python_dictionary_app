from django.http import HttpResponseBadRequest
from rest_framework import viewsets, views, mixins
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from dictionary.models import Word, Attempts
from dictionary.api.serializers import WordSerializer, AttemptsSerializer
import requests as req
from rest_framework import status
import json


class WordViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        name = request.data.__getitem__('name')

        try:
            word = Word.objects.get(name=name)
            serializer = self.get_serializer(word)
            message = 'the word already exists'
        except Word.DoesNotExist:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            word = Word.objects.get(name=name)
            message = 'the word was created'

        headers = self.get_success_headers(serializer.data)

        try:
            Attempts.objects.get(user=self.request.user, word=word)
            message += ", and was associated with the user"
        except Attempts.DoesNotExist:
            Attempts.objects.create(user=self.request.user, word=word)

        data = serializer.data
        data['message'] = message

        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


class AttemptsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    serializer_class = AttemptsSerializer
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Attempts.objects.all().filter(user=self.request.user)
        return queryset

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        new_hit = 0
        try:
            if request.data.__getitem__('success') is True:
                new_hit = 1
        except KeyError:
            return HttpResponseBadRequest()
        data = {'word': instance.word.pk, 'attempts': instance.attempts+1, 'hits': instance.hits+new_hit}
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class WordSearch(views.APIView):

    def get(self, request):
        word = request.GET.get('word', None)
        word_definition = req.get(f'https://googledictionaryapi.eu-gb.mybluemix.net/?define={word}&lang=en')
        data = json.loads(word_definition.text)
        return Response(data)
