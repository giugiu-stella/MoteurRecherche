import requests
from server.graph import UnweightedGraph, WeightedGraph
from server.centrality import *
from data.config import URL_BASE_DATA
from backend.config import URL_NEIGHBOR, URL_BASE, construct_url_requete_search

URL_REQUETE_NEIGHBOR = URL_BASE + URL_BASE_DATA + URL_NEIGHBOR
NUMBER_SUGGESTION = 10


def suggestion(book_ids):
    book_suggestion = []
    book_suggestion_id = set()
    number_book_in_suggestion = 0
    
    for identifiant in book_ids[:3]:  
        url_requete = construct_url_requete_search(URL_REQUETE_NEIGHBOR) + str(identifiant)
        results = requests.get(url_requete)
        if results.status_code != 200:
            continue
        
        for book in results.json():
            if book['id'] not in book_suggestion_id and book['id'] not in book_ids:
                number_book_in_suggestion += 1
                book_suggestion.append(book)
                if number_book_in_suggestion >= NUMBER_SUGGESTION:
                    return book_suggestion
        
    return book_suggestion


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def sort_by_centrality(search, centrality, ordre):
    G = UnweightedGraph() if centrality == Centrality.BETWEENNESS else WeightedGraph()
    for book in search:
        G.add_node(book)
    
    for n in G.nodes:
        for m in G.nodes:
            if n == m or m in n.neighbors:
                continue
            
            weight = len(intersection(m.json["subjects"], n.json["subjects"]))
            if weight > 0:
                if centrality == Centrality.BETWEENNESS :
                    G.add_edge(n, m)
                else:
                    G.add_edge(n, m, weight)
        
    if centrality == Centrality.BETWEENNESS:
        compute_betweenness_centrality(G)
    else:
        compute_closeness_centrality(G)
    G.sort_nodes_by_centrality_measure(ordre)
    
    return [n.json for n in G.nodes]

