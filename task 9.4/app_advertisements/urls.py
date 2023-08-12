from django.urls import path
from .views import example, top_sellers

urlpatterns = [
    path("", example, name = "main-page"),
    path("top-sellers/", top_sellers, name="top-sellers")
]
