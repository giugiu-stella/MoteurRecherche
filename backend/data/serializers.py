from rest_framework import serializers
from data.models import *


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
    language = LanguageSerializer()
    subjects = serializers.SerializerMethodField()

    lookup_field = 'gutenberg_id'

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'authors',
            'subjects',
            'language',
            'cover_image',
            'plain_text',
            'download_count'
        )

    def get_id(self, book):
        return book.gutenberg_id

    """def get_language(self, book):
        return book.language.code"""

    def get_subjects(self, book):
        subjects = [subject.name for subject in book.subjects.all()]
        #subjects.sort()
        return subjects
