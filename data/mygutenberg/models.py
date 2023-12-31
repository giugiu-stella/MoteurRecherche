from django.db import models

# Create your models here.


class Book(models.Model):
    gutenberg_id = models.PositiveIntegerField(primary_key=True)
    authors = models.ManyToManyField('Person')
    download_count = models.PositiveIntegerField(blank=True, null=True)
    languages = models.ManyToManyField('Language')
    subjects = models.ManyToManyField('Subject')
    title = models.CharField(blank=True, max_length=1024, null=True, db_index=True)
    cover_image = models.URLField(default='')
    plain_text = models.URLField(default='')
    
    class Meta:
        indexes = [
            models.Index(fields=['title']),
        ]


class Language(models.Model):
    code = models.CharField(max_length=4, unique=True)


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
