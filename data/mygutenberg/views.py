from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from mygutenberg.models import Book
from mygutenberg.serializers import BookSerializer

# Create your views here.


class BookList(APIView):
    """
    List all books.
    """
    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class BookDetail(APIView):
    """
    Retrieve a Book instance.
    """
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)


class LanguageBookList(APIView):
    def get(self, request, language, format=None):
        english_books = Book.objects.filter(languages__code=language)
        serializer = BookSerializer(english_books, many=True)
        return Response(serializer.data)


class TitleBookList(APIView):
    def get(self, request, title, format=None):
        resultats = Book.objects.filter(title__icontains=title)
        serializer = BookSerializer(resultats, many=True)
        return Response(serializer.data)
    
    
class TitleRegexBookList(APIView):
    def get(self, request, title, format=None):
        resultats = Book.objects.filter(title__regex=title)
        serializer = BookSerializer(resultats, many=True)
        return Response(serializer.data)
    
class AuthorNameBookList(APIView):
    def get(self, request, name, format=None):
        resultats = Book.objects.filter(authors__name__icontains=name)
        serializer = BookSerializer(resultats, many=True)
        return Response(serializer.data)
    
class AuthorRegexNameBookList(APIView):
    def get(self, request, name, format=None):
        resultats = Book.objects.filter(authors__name__regex=name)
        serializer = BookSerializer(resultats, many=True)
        return Response(serializer.data)
    