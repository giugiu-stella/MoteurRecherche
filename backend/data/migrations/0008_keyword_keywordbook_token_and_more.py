# Generated by Django 4.2.9 on 2024-01-29 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("data", "0007_neighbors"),
    ]

    operations = [
        migrations.CreateModel(
            name="Keyword",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("occurence", models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="KeywordBook",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Token",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("token", models.CharField(db_index=True, max_length=128)),
            ],
        ),
        migrations.RemoveIndex(
            model_name="book",
            name="data_book_title_9ade21_idx",
        ),
        migrations.AddField(
            model_name="book",
            name="chemin_text",
            field=models.FilePathField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name="book",
            name="cover_image",
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name="book",
            name="plain_text",
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name="keywordbook",
            name="book",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="data.book"
            ),
        ),
        migrations.AddField(
            model_name="keywordbook",
            name="keywords",
            field=models.ManyToManyField(to="data.keyword"),
        ),
        migrations.AddField(
            model_name="keyword",
            name="token",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="data.token"
            ),
        ),
    ]