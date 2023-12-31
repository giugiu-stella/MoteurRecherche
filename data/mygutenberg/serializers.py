from rest_framework import serializers
from mygutenberg.models import *


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('code',)


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'birth_year', 'death_year')


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('name',)


class BookSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    authors = PersonSerializer(many=True)
    languages = serializers.SerializerMethodField()
    subjects = serializers.SerializerMethodField()

    lookup_field = 'gutenberg_id'

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'authors',
            'subjects',
            'languages',
            'cover_image',
            'plain_text',
            'download_count'
        )

    def get_id(self, book):
        return book.gutenberg_id

    def get_languages(self, book):
        languages = [language.code for language in book.languages.all()]
        languages.sort()
        return languages

    def get_subjects(self, book):
        subjects = [subject.name for subject in book.subjects.all()]
        subjects.sort()
        return subjects
