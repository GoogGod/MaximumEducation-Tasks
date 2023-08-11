from django.urls import path

from .views import request


urlpatterns = [
    path('', request),
]
