import requests
from server.graph import Graph, Node
from data.config import URL_BASE_DATA
from backend.config import URL_NEIGHBOR, URL_BASE, construct_url_requete_search

URL_REQUETE_NEIGHBOR = URL_BASE + URL_BASE_DATA + URL_NEIGHBOR
NUMBER_SUGGESTION = 10

#Sort by popularity
def sort(search):
    #book_sorted = sort_by_popularity(search)
    book_sorted = sort_by_betwenness_centrality(search)

    return {"result" : book_sorted, "suggestion" : suggestion(book_sorted)}


def sort_mot_cle_contenu(search, mot) :
    ListNomOccurence = []
    for json in search:
        ListNomOccurence.append((getTitle(json), getOccurencesText(getText(json), mot)))
        
    livres_tries = sort_list_search(ListNomOccurence,lambda x: x[1])
    
    return livres_tries


#Trie une liste de manière décroissante en utilisant la fonction f pour décider l'ordre entre les éléments
def sort_list_search(search, f):
    return sorted(search, key=f, reverse=True)

def sort_by_popularity(search):
    return sort_list_search(search, lambda x: x["download_count"])
    
def getText(json):
    url_text = json["plain_text"]
    return requests.get(url_text).text

def getTitle(json):
    return json["title"]

def getOccurencesText(text,compare) :
    listText = text.lower().split()
    return listText.count(compare.lower())

def suggestion(result_search):
    book_suggestion = []
    book_suggestion_id = set()
    number_book_in_suggestion = 0
    id_result_search = [book['id'] for book in result_search]
    
    for n in result_search:  
        url_requete = construct_url_requete_search(URL_REQUETE_NEIGHBOR) + str(n['id'])
        results = requests.get(url_requete)
        
        for book in results.json():
            if book['id'] not in book_suggestion_id and book['id'] not in id_result_search:
                number_book_in_suggestion += 1
                book_suggestion.append(book)
                if number_book_in_suggestion >= NUMBER_SUGGESTION:
                    return book_suggestion
        
    return book_suggestion


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def sort_by_betwenness_centrality(search):
    G = Graph()
    for book in search:
        G.add_node(book)
    
    for n in G.nodes:
        for m in G.nodes:
            if n == m or m in n.neighbors:
                continue
            
            if intersection(m.json["subjects"], n.json["subjects"]) != []:
                G.add_edge(n, m)
        
    G.calculate_betweenness_centrality()
    G.sort_nodes_by_centrality_measure()
    
    return [n.json for n in G.nodes]

if __name__ == "__main__":
    print(construct_url_requete_search(URL_REQUETE_NEIGHBOR))