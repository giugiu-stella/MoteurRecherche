from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from data.config import URL_BASE_DATA
from server.config import URL_BASE_SERVER
from server.sort import sort_by_centrality, suggestion
from server.centrality import Centrality



class BooksList(APIView):
    def get(self, request, format=None):
        url = request.build_absolute_uri()
        url = url.replace(URL_BASE_SERVER, URL_BASE_DATA)
        
        results = requests.get(url)

        results = results.json()
        
        sort = self.request.GET.get('sort')
        ordre = request.GET.get('order')
        ordre = "descending" if ordre is None else ordre
        
        if sort == 'closeness':
            results = sort_by_centrality(results, Centrality.CLOSENESS, ordre)
        elif sort == 'betweenness':
            results = sort_by_centrality(results, Centrality.BETWEENNESS, ordre)
          
        results = {"result" : results, "suggestion" : suggestion([b['id'] for b in results])}

        return Response(results)

    
    