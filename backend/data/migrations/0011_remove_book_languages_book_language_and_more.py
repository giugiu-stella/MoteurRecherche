# Generated by Django 4.2.9 on 2024-01-30 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("data", "0010_alter_neighbors_book"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="languages",
        ),
        migrations.AddField(
            model_name="book",
            name="language",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="data.language",
            ),
        ),
        migrations.AlterField(
            model_name="neighbors",
            name="book",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="data.book"
            ),
        ),
    ]
