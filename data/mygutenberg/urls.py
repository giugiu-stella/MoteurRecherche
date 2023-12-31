from django.urls import path
from mygutenberg import views

urlpatterns = [
    path('books/', views.BookList.as_view()),
    path('book/<int:pk>/', views.BookDetail.as_view()),
    path('languagebooks/<str:language>/', views.LanguageBookList.as_view()),
    path('namebooks/<str:name_recherche>/', views.NameBookList.as_view()),
    path('nameauthorsbooks/<str:name_recherche>/', views.AuthorNameBookList.as_view()),
    
]
