from django.test import TestCase

# Create your tests here.
# nombre keywords 2162964
            
"""from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
import requests 
#from jaccard import tokenarisation
from nltk.corpus import stopwords"""
import spacy
import os
import json

#print(os.getcwd())
np_en = spacy.load('en_core_web_sm')
DOM = '\ufeff'
def enleve_dom(document):
    # enlève le DOM
    if len(document) > 0 and document[0] == DOM:
        document = document[1:]
        
def get_keyword(document):
    texts = document.split("\n\n")
    
    res = set()              

    for text in texts:
        doc = np_en(text)
        keywords = {token.lemma_.casefold() for token in doc if (token.is_alpha or token.is_digit) and not(token.is_stop)}
        res.update(keywords)
    return res
                

def get_keyword_token(token):
    res = set()
    for t in token :
        doc = np_en(t)
        doc = doc[0]
        if (doc.is_alpha or doc.is_digit) and not(doc.is_stop):
            res.add(doc.lemma_.casefold())
    return res

dossier_occu = "./keywords/"
chemin_fichier_occu = os.path.join(dossier_occu, "46.json")

with open(chemin_fichier_occu, "r") as fichier:
    token = json.load(fichier)
    
dossier_text  = "./books/"
chemin_fichier_text = os.path.join(dossier_text, "46.txt")

with open(chemin_fichier_occu, "r") as fichier:
    document = fichier.read()

keyword_token = get_keyword_token(token.keys())
keyword_doc = get_keyword(document)

for k in keyword_token:
    if k not in keyword_doc:
        print(k)

"""set(stopwords.words("en"))

lemmatizer = WordNetLemmatizer()
# Initialisation du stemmer
porter_stemmer = PorterStemmer()

# Exemple de document

url = "https://www.gutenberg.org/cache/epub/64317/pg64317.txt"
document = requests.get(url).text



# Tokenisation du document en mots
words = word_tokenize(document.casefold())
print(f"words {len(set(words))}")
stop_words = set(stopwords.words("english"))

filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
print(f"without stop words {len(set(filtered_words))}")
lemme = [lemmatizer.lemmatize(word) for word in filtered_words]
print(f"lemme {len(set(lemme))}")"""
#words = [w for w in words if len(w) >= 3]

"""np_en = spacy.load('en_core_web_sm')
doc = np_en(document)
keywords = {token.lemma_.casefold() for token in doc if token.is_alpha and not(token.is_stop)}
print(len(keywords))"""

"""words_2 = tokenarisation(document)
print(f"words_2 {len(set(words_2))}")
lemme_2 = [lemmatizer.lemmatize(word) for word in words_2]

for w1, w2 in zip(words_2, lemme_2):
    if w1 != w2:
        print(f"{w1} {w2}")"""

"""print(words[:100])
print(words_2[:100])"""
"""
print("stem")

print([porter_stemmer.stem(word) for word in words][:100])
print()"""

"""print([porter_stemmer.stem(word) for word in words_2][:100])
print()
print()

print("lemme")
#print([lemmatizer.lemmatize(word) for word in words][:100])
#print()
print([lemmatizer.lemmatize(word) for word in words_2][:100])"""
"""# Calcul du radical pour chaque mot
stems = [porter_stemmer.stem(word) for word in words]

# Affichage des résultats
print("Document original:", document)
print(words)
print("Radicaux des mots:", stems)
print([lemmatizer.lemmatize(w) for w in words])
"""