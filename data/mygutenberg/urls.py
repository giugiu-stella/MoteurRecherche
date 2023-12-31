from django.urls import path
from mygutenberg import views

urlpatterns = [
    path('books/', views.BookList.as_view()),
    path('book/<int:pk>/', views.BookDetail.as_view()),
    path('books/language/<str:language>/', views.LanguageBookList.as_view()),
    path('books/title/<str:title>/', views.TitleBookList.as_view()),
    path('books/regex/title/<str:title>/', views.TitleRegexBookList.as_view()),
    path('books/authors/name/<str:name>/', views.AuthorNameBookList.as_view()),
    path('books/regex/authors/name/<str:name>/', views.AuthorRegexNameBookList.as_view()),
]
