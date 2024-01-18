from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from backend.config import *
from data.config import URL_BASE_DATA
from server.sort import sort

URL_BASE_REQUETE = URL_BASE + URL_BASE_DATA

def construct_url_requete_data(url):
    return URL_BASE_REQUETE + url

def redirect_data(url_end_requete, search_argument : str = None):
    if search_argument is not None:
        url_end_requete = construct_url_requete_search(url_end_requete) + search_argument
    url_requete = construct_url_requete_data(url_end_requete)
    results = requests.get(url_requete)
    return results.json()

def redirect_data_sort(url_end_requete, search_argument=None):
    results_search = redirect_data(url_end_requete, search_argument)
    result_sort = sort(results_search)
    return Response(result_sort)


class BookList(APIView):
    """
    List all books.
    """
    def get(self, request, format=None):
        return redirect_data_sort(URL_SEARCH_BOOKS)


class BookDetail(APIView):
    def get(self, request, pk, format=None):
        result_search = redirect_data(URL_SEARCH_BOOK_ID, str(pk))
        return Response(result_search)

class TitleBookList(APIView):
    def get(self, request, title, format=None):
        return redirect_data_sort(URL_SEARCH_BOOKS_TITLE, title)
    
class TitleRegexBookList(APIView):
    def get(self, request, title, format=None):
        return redirect_data_sort(URL_SEARCH_BOOKS_TITLE, title)
    
class LanguageBookList(APIView):
    def get(self, request, language, format=None):
        return redirect_data_sort(URL_SEARCH_BOOKS_LANGUAGE, language)
    
class AuthorNameBookList(APIView):
    def get(self, request, name, format=None):
        return redirect_data_sort(URL_SEARCH_BOOKS_NAME_AUTHOR, name)
    
class AuthorRegexNameBookList(APIView):
    def get(self, request, name, format=None):
        return redirect_data_sort(URL_SEARCH_REGEX_BOOKS_NAME_AUTHOR, name)
    
    