from django.urls import path
from mygutenberg import views

urlpatterns = [
    path('books/', views.BookList.as_view()),
    path('book/<int:pk>/', views.BookDetail.as_view()),
    path('englishbooks/', views.EnglishBookList.as_view())
]
