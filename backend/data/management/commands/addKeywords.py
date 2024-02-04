from django.core.management.base import BaseCommand
from data.models import *
import os
import json

dossier_occu = 'keywords'

class Command(BaseCommand):
    help = 'add keywords'
    
    def handle(self, *args, **options):
        keywords = dict()
        keywords_code = {'en' : set(), 'fr' : set()}
        for nom_fichier in os.listdir(dossier_occu):
            chemin_fichier = os.path.join(dossier_occu, nom_fichier)
            pk = int(nom_fichier.split('.')[0])
            with open(chemin_fichier, 'r') as f:
                keywords_book = json.load(f)
                book = Book.objects.get(pk=pk)
            for k, occ in keywords_book.items():
                if k not in keywords:
                    keywords_code[book.language.code].add(k)
                    keywords[k] = {(book, occ)}
                else:
                    keywords[k].add((book, occ))
           
                   
        for k in keywords_code['en']:      
            key_en = KeywordsEnglish.objects.create(token=k)
            for (b, occu) in keywords[k]:
                KeywordBookEnglish.objects.create(book=b, occurence=occu, keyword=key_en)
                key_en.books.add(b)
            
            
        for k in keywords_code['fr']:
            key_fr = KeywordsFrench.objects.create(token=k)
            for (b, occu) in keywords[k]:
                KeywordBookFrench.objects.create(book=b, occurence=occu, keyword=key_fr)
                key_fr.books.add(b)         
    