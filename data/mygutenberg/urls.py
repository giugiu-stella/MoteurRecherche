from django.urls import path
from mygutenberg import views
from mygutenberg.config import URL_BASE_DATA
from data.config import *


def construct_url_data(url):
    return URL_BASE_DATA + url

urlpatterns = [
    path(construct_url_data(URL_SEARCH_BOOKS), views.BookList.as_view()),
    path(construct_url_data(URL_SEARCH_BOOK_ID), views.BookDetail.as_view()),
    path(construct_url_data(URL_SEARCH_BOOKS_LANGUAGE), views.LanguageBookList.as_view()),
    path(construct_url_data(URL_SEARCH_BOOKS_TITLE), views.TitleBookList.as_view()),
    path(construct_url_data(URL_SEARCH_REGEX_BOOKS_TITLE), views.TitleRegexBookList.as_view()),
    path(construct_url_data(URL_SEARCH_BOOKS_NAME_AUTHOR), views.AuthorNameBookList.as_view()),
    path(construct_url_data(URL_SEARCH_REGEX_BOOKS_NAME_AUTHOR), views.AuthorRegexNameBookList.as_view()),
]
