import requests
from Jaccard import distance_jaccard

#voir Jaccard.py

def sort(search):
    print(len(search))
    return sort_by_popularity(search)

def sort_par_titre(search):
    ListNomDist = []
    comparatif = getTitle(search[0])
    for json in search:
        #la division sert � normaliser la distance pour limiter l'impact de la longueur de la String mais �a ne marche pas super bien
        ListNomDist.append((getTitle(json), distance_jaccard(comparatif, getTitle(json)) / ((len(comparatif.split()) + len(getTitle(json).split())) / 2)))
        
    livres_tries = sorted(ListNomDist, key=lambda x: x[1])
    
    return livres_tries

def sort_mot_cle_contenu(search, mot) :
    ListNomOccurence = []
    for json in search:
        ListNomOccurence.append((getTitle(json), getOccurencesText(getText(json), mot)))
        
    livres_tries = sort_list_search(ListNomOccurence,lambda x: x[1])
    
    return livres_tries


#Trie une liste de manière décroissante en utilisant la fonction pour décider l'ordre entre les éléments
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




test = [{
    "id": 84,
    "title": "Frankenstein; Or, The Modern Prometheus",
    "authors": [
        {
            "name": "Shelley, Mary Wollstonecraft",
            "birth_year": 1797,
            "death_year": 1851
        }
    ],
    "subjects": [
        "Frankenstein's monster (Fictitious character) -- Fiction",
        "Frankenstein, Victor (Fictitious character) -- Fiction",
        "Gothic fiction",
        "Horror tales",
        "Monsters -- Fiction",
        "Science fiction",
        "Scientists -- Fiction"
    ],
    "languages": [
        "en"
    ],
    "cover_image": "https://www.gutenberg.org/cache/epub/84/pg84.cover.medium.jpg",
    "plain_text": "https://www.gutenberg.org/ebooks/84.txt.utf-8",
    "download_count": 91860
},{
    "id": 84,
    "title": "test de titre gogogo",
    "authors": [
        {
            "name": "Shelley, Mary Wollstonecraft",
            "birth_year": 1797,
            "death_year": 1851
        }
    ],
    "subjects": [
        "Frankenstein's monster (Fictitious character) -- Fiction",
        "Frankenstein, Victor (Fictitious character) -- Fiction",
        "Gothic fiction",
        "Horror tales",
        "Monsters -- Fiction",
        "Science fiction",
        "Scientists -- Fiction"
    ],
    "languages": [
        "en"
    ],
    "cover_image": "https://www.gutenberg.org/cache/epub/84/pg84.cover.medium.jpg",
    "plain_text": "https://www.gutenberg.org/ebooks/145.txt.utf-8",
    "download_count": 91860
},{
    "id": 84,
    "title": "Le retour de Frankenstein",
    "authors": [
        {
            "name": "Shelley, Mary Wollstonecraft",
            "birth_year": 1797,
            "death_year": 1851
        }
    ],
    "subjects": [
        "Frankenstein's monster (Fictitious character) -- Fiction",
        "Frankenstein, Victor (Fictitious character) -- Fiction",
        "Gothic fiction",
        "Horror tales",
        "Monsters -- Fiction",
        "Science fiction",
        "Scientists -- Fiction"
    ],
    "languages": [
        "en"
    ],
    "cover_image": "https://www.gutenberg.org/cache/epub/84/pg84.cover.medium.jpg",
    "plain_text": "https://www.gutenberg.org/ebooks/1342.txt.utf-8",
    "download_count": 91860
}]

print(sort_mot_cle_contenu(test, "Science"))
#print(sort_par_titre(test))