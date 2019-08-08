from rest_framework import routers
from dictionary.api.viewsets import WordViewSet

router = routers.DefaultRouter()
router.register('words', WordViewSet, base_name='words')
