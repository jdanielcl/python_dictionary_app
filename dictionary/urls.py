from django.urls import path
from dictionary.views import index

urlpatterns = [
    path('', index, name="index")
]