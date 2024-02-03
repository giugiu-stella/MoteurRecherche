from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Language(models.Model):
    code = models.CharField(max_length=4, unique=True)


class Book(models.Model):
    gutenberg_id = models.PositiveIntegerField(primary_key=True)
    authors = models.ManyToManyField('Person')
    download_count = models.PositiveIntegerField(blank=True, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)
    #languages = models.ManyToManyField('Language')
    subjects = models.ManyToManyField('Subject')
    title = models.CharField(blank=True, max_length=1024, null=True)
    cover_image = models.URLField(max_length=1024,blank=True, null=True)
    plain_text = models.URLField(max_length=1024, blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['title'])
        ]


class Person(models.Model):
    birth_year = models.SmallIntegerField(blank=True, null=True)
    death_year = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=128)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]

class Subject(models.Model):
    name = models.CharField(max_length=256)

class Neighbors(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    #book = models.ForeignKey('Book', related_name='neighbors_as_book', on_delete=models.CASCADE)
    neighbors = models.ManyToManyField('Book', related_name='neighbors_as_neighbor')
    
    class Meta:
        indexes = [
            models.Index(fields=['book'])
        ]

class Keywords(models.Model):
    token = models.CharField(max_length=128, db_index=True, unique=True)
    
    class Meta:
        abstract = True
        indexes = [
            models.Index(fields=['token'])
        ]
    
class KeywordBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    occurence = models.PositiveIntegerField()
    
    class Meta:
        abstract = True
        
    
class KeywordsEnglish(Keywords):
    books = models.ManyToManyField('Book', through='KeywordBookEnglish')
    
class KeywordBookEnglish(KeywordBook):
    keyword = models.ForeignKey(KeywordsEnglish, on_delete=models.CASCADE)

class KeywordsFrench(Keywords):
    books = models.ManyToManyField('Book', through='KeywordBookFrench')
    
class KeywordBookFrench(KeywordBook):
    keyword = models.ForeignKey(KeywordsFrench, on_delete=models.CASCADE)