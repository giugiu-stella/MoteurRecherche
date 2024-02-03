from server import views
from django.urls import path
from backend.config import *
from server.config import *


def construct_url_server(url):
    return URL_BASE_SERVER + url

urlpatterns = [
    path(construct_url_server(URL_SEARCH_BOOKS), views.BooksList.as_view()),
]