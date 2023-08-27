from django.urls import path
from .views import example, top_sellers, advertisement_post

urlpatterns = [
    path("", example, name = "main-page"),
    path("top-sellers/", top_sellers, name="top-sellers"),
    path("advertisment-post/", advertisement_post, name="adv-post")
]
