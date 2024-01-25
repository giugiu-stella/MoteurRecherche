URL_BASE = 'http://127.0.0.1:8000/'
URL_SEARCH_BOOKS = 'books/'
URL_SEARCH_BOOK_ID = 'book/<int:pk>/'
URL_SEARCH_BOOKS_TITLE = 'books/title/<str:title>/'
URL_SEARCH_BOOKS_LANGUAGE =  'books/language/<str:language>/'
URL_SEARCH_REGEX = 'books/regex/'
URL_SEARCH_REGEX_BOOKS_TITLE = URL_SEARCH_REGEX + 'title/<str:title>/'
URL_SEARCH_BOOKS_NAME_AUTHOR = 'books/authors/name/<str:name>/'
URL_SEARCH_REGEX_BOOKS_NAME_AUTHOR = URL_SEARCH_REGEX + 'authors/name/<str:name>/'
URL_NEIGHBOR = "books/neighbors/<int:pk>"

def construct_url_requete_search(url : str) -> str:
    return url.split('<')[0]