# Generated by Django 5.0 on 2024-02-03 18:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("data", "0011_remove_book_languages_book_language_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="chemin_text",
        ),
    ]