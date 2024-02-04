from django.core.management import BaseCommand
from data.models import *
import requests
from data.jaccard import jaccard_distance
import time
import json
import os

JACCARD_DISTANCE_THRESHOLD = 0.4




class Command(BaseCommand):
    help = 'Create the jaccard graph'

    def add_as_neighbor(self, pk1, pk2):
        l1 = Book.objects.get(pk=pk1)
        l2 = Book.objects.get(pk=pk2)
        
        Neighbors.objects.create(book=l1, neighbor=l2)
        Neighbors.objects.create(book=l2, neighbor=l1)
        self.stdout.write(self.style.SUCCESS('['+time.ctime()+f'] Successfully added the book {pk1} and book {pk2} as neighbor'))
    
    def handle(self, *args, **options):
        books_occurences = dict()
        #using  json file
        dossier_occu = "./keywords/"
        for nom_fichier in os.listdir(dossier_occu):
            chemin_fichier = os.path.join(dossier_occu, nom_fichier)

            with open(chemin_fichier, "r") as fichier:
                token = json.load(fichier)
                
            pk = int(nom_fichier.split('.')[0])
            books_occurences[pk] = token
        

        self.stdout.write('['+time.ctime()+'] Creating the jaccard graph...')
        neighbor = {pk : [] for pk in books_occurences.keys()}
        
        for pk in books_occurences.keys():
            tokens = books_occurences[pk]
            book_neighbor = neighbor[pk]
                
            for pk2 in books_occurences.keys():
                if pk2 in book_neighbor or pk == pk2:
                    continue
                if jaccard_distance(tokens, books_occurences[pk2]) < JACCARD_DISTANCE_THRESHOLD:
                    self.add_as_neighbor(pk, pk2)
                    if pk2 not in neighbor:
                        neighbor[pk2] = {pk}
                    else:
                        neighbor[pk2].append(pk)
                        
            self.stdout.write(self.style.SUCCESS('['+time.ctime()+'] Successfully added the neighbors for book id="%s"' % pk))
        self.stdout.write('['+time.ctime()+'] End of Jaccard graph creation.')