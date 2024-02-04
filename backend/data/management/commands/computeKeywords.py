from django.core.management.base import BaseCommand
from data.models import *
import spacy
import os
from collections import Counter
import json

DOM = '\ufeff'
dossier_books = 'books'
dossier_token = "token"

class Command(BaseCommand):
    help = 'Extract keyword from the books'
    def handle(self, *args, **options):
        
        nlp  = {'en' : spacy.load('en_core_web_sm'), 'fr' : spacy.load('fr_core_news_sm')}
        for book in Book.objects.all() :
            code = book.languages.all()[0].code
            str_pk = str(book.pk)
            chemin_fichier = os.path.join(dossier_books, str_pk + ".txt")
            with open(chemin_fichier, "r") as fichier:
                document = fichier.read()
                    
            texts = document.split("\n\n")
            keywords_doc = []
            
            for text in texts:
                doc = nlp[code](text)
                keywords_doc.extend([token.lemma_.casefold() for token in doc if token.is_alpha and not(token.is_stop)])
                
            dossier_occu = "./keywords/"
            chemin_fichier = os.path.join(dossier_occu, str_pk + ".json")

            with open(chemin_fichier, "w") as fichier:
                json.dump(Counter(keywords_doc),fichier)
                    
            