import requests
import Jaccard

#voir Jaccard.py

def sort_par_titre(search):
    ListNomDist = []
    comparatif = getTitle(search[0])
    for json in search:
        #la division sert à normaliser la distance pour limiter l'impact de la longueur de la String mais ça ne marche pas super bien
        ListNomDist.append((getTitle(json), Jaccard.distance_jaccard(comparatif, getTitle(json)) / ((len(comparatif.split()) + len(getTitle(json).split())) / 2)))
        
    livres_tries = sorted(ListNomDist, key=lambda x: x[1])
    
    return livres_tries


def getText(json):
    url_text = json["plain_text"]
    return requests.get(url_text).text

def getTitle(json):
    return json["title"]


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
    "plain_text": "https://www.gutenberg.org/ebooks/84.txt.utf-8",
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
    "plain_text": "https://www.gutenberg.org/ebooks/84.txt.utf-8",
    "download_count": 91860
}]


print(sort_par_titre(test))