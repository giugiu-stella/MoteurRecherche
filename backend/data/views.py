from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.http import Http404
from data.models import Book, Neighbors, KeywordsEnglish, KeywordsFrench
from data.serializers import BookSerializer

# Create your views here.


class BookViewSet(APIView):
    
    def get(self, request, format=None):
        queryset = Book.objects.exclude(download_count__isnull=True)
        queryset = queryset.exclude(title__isnull=True)
        
        language = request.GET.get('language')
        if language is not None:
            queryset = queryset.filter(language__code=language)
        
        search_name_author = request.GET.get('author_name')
        if search_name_author is not None:
            search_name_authors_type = request.GET.get('author_name_type')
            search_name_authors_type = "classique" if search_name_authors_type is None else search_name_authors_type
            
            if search_name_authors_type == "classique":
                queryset = queryset.filter(authors__name__icontains=search_name_author)
            else:
                queryset = queryset.filter(authors__name__regex=search_name_author)
                
        search_title = request.GET.get('title')
        if search_title is not None:
            search_title_type = request.GET.get('title_type')
            
            search_title_type = "classique" if search_title_type is None else search_title_type
            if search_title_type == "classique":
                queryset = queryset.filter(title__icontains=search_title)
            else:
                queryset = queryset.filter(title__regex=search_title)
                
        search_keyword = request.GET.get('keyword')
        if search_keyword is not None:
            
            search_keywords_type = request.GET.get('keyword_type')
            search_keywords_type = "classique" if search_keywords_type is None else search_keywords_type
            
            if language is not None:
                if language == 'en':
                    if search_keywords_type == "classique":
                        queryset = queryset.filter(keywordsenglish__token__icontains=search_keyword)
                    else:
                        queryset = queryset.filter(keywordsenglish__token__regex=search_keyword)
                elif language == 'fr':
                    if search_keywords_type == "classique":
                        queryset = queryset.filter(keywordsfrench__token__icontains=search_keyword)
                    else:
                         queryset = queryset.filter(keywordsfrench__token__regex=search_keyword)
                else:
                    if search_keywords_type == "classique":
                        queryset = queryset.filter(keywordsfrench__token__icontains=search_keyword)
                        queryset = queryset.filter(keywordsenglish__token__icontains=search_keyword)
                    else:
                        queryset = queryset.filter(keywordsfrench__token__regex=search_keyword)
                        queryset = queryset.filter(keywordsenglish__token__regex=search_keyword)
                
            else:
                if search_keywords_type == "classique":
                    queryset = queryset.filter(keywordsfrench__token__icontains=search_keyword)
                    queryset = queryset.filter(keywordsenglish__token__icontains=search_keyword)
                else:
                    queryset = queryset.filter(keywordsfrench__token__regex=search_keyword)
                    queryset = queryset.filter(keywordsenglish__token__regex=search_keyword)
        
        sort = request.GET.get('sort')
        if sort == 'download_count':
            ord = request.GET.get('order')
            ord = "descending" if ord is None else ord
            if ord == "descending":
                queryset = queryset.order_by('-download_count')
            else:
                queryset = queryset.order_by('download_count')    
            
        queryset.distinct()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

        
    
class NeighboorsBook(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        try:
            book_voisins = Neighbors.objects.get(book=book)
        except Neighbors.DoesNotExist:
            return Response([])

        voisins = book_voisins.neighbors.all()
        serializer = BookSerializer(voisins, many=True)
        return Response(serializer.data)    
    