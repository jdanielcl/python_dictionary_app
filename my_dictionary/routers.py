from rest_framework import routers
from dictionary.api.viewsets import WordViewSet, AttemptsViewSet

router = routers.DefaultRouter()
router.register('words', WordViewSet, base_name='words')
router.register('attempts', AttemptsViewSet, base_name='attempts')
