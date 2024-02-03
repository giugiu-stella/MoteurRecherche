from data import views
from django.urls import path
from backend.config import *
from data.config import *


def construct_url_data(url):
    return URL_BASE_DATA + url

urlpatterns = [
    path(construct_url_data(URL_SEARCH_BOOKS), views.BookViewSet.as_view()),
    path(construct_url_data(URL_NEIGHBOR), views.NeighboorsBook.as_view()),
]