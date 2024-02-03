from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from data.config import URL_BASE_DATA
from server.config import URL_BASE_SERVER
from server.sort import sort_search, suggestion
from server.centrality import Centrality



class BooksList(APIView):
    def get(self, request, format=None):
        url = request.build_absolute_uri()
        url = url.replace(URL_BASE_SERVER, URL_BASE_DATA)
        #print(f"data {url}")
        results = requests.get(url)
        #print(results.status_code)
        results = results.json()
        
        sort = self.request.GET.get('sort')
        if sort == 'closeness':
            results = sort_search(results, Centrality.CLOSENESS)
        elif sort == 'betweenness':
            results = sort_search(results, Centrality.BETWEENNESS)
            
        {"result" : results, "suggestion" : suggestion([b['id'] for b in results])}
        return Response(results)
        #return Response(dict())

    
    