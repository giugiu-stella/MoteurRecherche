from django.core.management.base import BaseCommand
from mygutenberg.models import *
import json
import requests
import re
from mygutenberg.config import URL_INIT_BIBLIOTHEQUE, MIN_NB_LIVRE_BIBLIOTHEQUE, MIN_NB_MOTS_LIVRES
import time


def compter_mots(url_du_livre):
    fichier = requests.get(url_du_livre)
    fichier.raise_for_status()  # Lèvera une exception pour les codes d'erreur HTTP
    contenu = fichier.text
    mots = re.findall(r'\b\w+\b', contenu)
    nombre_de_mots = len(mots)
    return nombre_de_mots


def put_book_db(book):
    """Make/update the book."""
    book_in_db = Book.objects.create(
        gutenberg_id=book['id'],
        download_count=book['download_count'],
        title=book['title'],
        cover_image=book['formats']['image/jpeg'],
        plain_text=book['formats']['text/plain; charset=us-ascii']

    )

    """Make/update the authors."""

    authors = []
    for author in book['authors']:
        person = Person.objects.filter(
            name=author['name'],
            birth_year=author['birth_year'],
            death_year=author['death_year']
        )
        if person.exists():
            person = person[0]
        else:
            person = Person.objects.create(
                name=author['name'],
                birth_year=author['birth_year'],
                death_year=author['death_year']
            )
        authors.append(person)

    for author in authors:
        book_in_db.authors.add(author)

    ''' Make/update the languages. '''

    languages = []
    for language in book['languages']:
        language_in_db = Language.objects.filter(code=language)
        if language_in_db.exists():
            language_in_db = language_in_db[0]
        else:
            language_in_db = Language.objects.create(code=language)
        languages.append(language_in_db)

    for language in languages:
        book_in_db.languages.add(language)

    ''' Make/update subjects. '''

    subjects = []
    for subject in book['subjects']:
        subject_in_db = Subject.objects.filter(name=subject)
        if subject_in_db.exists():
            subject_in_db = subject_in_db[0]
        else:
            subject_in_db = Subject.objects.create(name=subject)
        subjects.append(subject_in_db)

    for subject in subjects:
        book_in_db.subjects.add(subject)


class Command(BaseCommand):
    help = 'Initialise the database'

    def handle(self, *args, **options):
        nb_livres = 0
        url = URL_INIT_BIBLIOTHEQUE

        while nb_livres < MIN_NB_LIVRE_BIBLIOTHEQUE:
            reponse = requests.get(url)
            json_data = reponse.json()

            for book in json_data['results']:
                try:
                    if compter_mots(book['formats']['text/plain; charset=us-ascii']) >= MIN_NB_MOTS_LIVRES:
                        print(book['title'])
                        put_book_db(book)
                        nb_livres += 1
                        self.stdout.write(self.style.SUCCESS(
                            '[' + time.ctime() + '] Successfully added book id="%s"' % book['id']))
                except requests.exceptions.HTTPError:
                    self.stdout.write(' Request Exception\n')
                    continue
                except KeyError as e:
                    print(f"Une KeyError s'est produite: {e}")
                    continue
                except Exception as error:
                    book_json = json.dumps(book, indent=4)
                    self.stdout.write(' Error while putting this book info in the database:\n',
                                      book_json,
                                      '\n'
                                      )
                    raise error

            if json_data['next'] is None:
                break
            url = json_data['next']
