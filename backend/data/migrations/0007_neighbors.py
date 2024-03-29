# Generated by Django 5.0 on 2024-01-24 23:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("data", "0006_delete_graphjaccard"),
    ]

    operations = [
        migrations.CreateModel(
            name="Neighbors",
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
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="neighbors_as_book",
                        to="data.book",
                    ),
                ),
                (
                    "neighbor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="neighbors_as_neighbor",
                        to="data.book",
                    ),
                ),
            ],
        ),
    ]
