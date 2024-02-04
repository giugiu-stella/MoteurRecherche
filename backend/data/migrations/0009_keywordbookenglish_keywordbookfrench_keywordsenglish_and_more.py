# Generated by Django 4.2.9 on 2024-01-30 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("data", "0008_keyword_keywordbook_token_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="KeywordBookEnglish",
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
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="KeywordBookFrench",
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
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="KeywordsEnglish",
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
                ("token", models.CharField(db_index=True, max_length=128, unique=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="KeywordsFrench",
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
                ("token", models.CharField(db_index=True, max_length=128, unique=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.RemoveField(
            model_name="keyword",
            name="token",
        ),
        migrations.RemoveField(
            model_name="keywordbook",
            name="book",
        ),
        migrations.RemoveField(
            model_name="keywordbook",
            name="keywords",
        ),
        migrations.RemoveField(
            model_name="neighbors",
            name="neighbor",
        ),
        migrations.AddField(
            model_name="neighbors",
            name="neighbors",
            field=models.ManyToManyField(
                related_name="neighbors_as_neighbor", to="data.book"
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="title",
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name="neighbors",
            name="book",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="data.book"
            ),
        ),
        migrations.AddIndex(
            model_name="book",
            index=models.Index(fields=["title"], name="data_book_title_9ade21_idx"),
        ),
        migrations.AddIndex(
            model_name="neighbors",
            index=models.Index(fields=["book"], name="data_neighb_book_id_bb5826_idx"),
        ),
        migrations.DeleteModel(
            name="Keyword",
        ),
        migrations.DeleteModel(
            name="KeywordBook",
        ),
        migrations.DeleteModel(
            name="Token",
        ),
        migrations.AddField(
            model_name="keywordsfrench",
            name="books",
            field=models.ManyToManyField(
                through="data.KeywordBookFrench", to="data.book"
            ),
        ),
        migrations.AddField(
            model_name="keywordsenglish",
            name="books",
            field=models.ManyToManyField(
                through="data.KeywordBookEnglish", to="data.book"
            ),
        ),
        migrations.AddField(
            model_name="keywordbookfrench",
            name="book",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="data.book"
            ),
        ),
        migrations.AddField(
            model_name="keywordbookfrench",
            name="keyword",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="data.keywordsfrench"
            ),
        ),
        migrations.AddField(
            model_name="keywordbookenglish",
            name="book",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="data.book"
            ),
        ),
        migrations.AddField(
            model_name="keywordbookenglish",
            name="keyword",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="data.keywordsenglish"
            ),
        ),
        migrations.AddIndex(
            model_name="keywordsfrench",
            index=models.Index(fields=["token"], name="data_keywor_token_ca4186_idx"),
        ),
        migrations.AddIndex(
            model_name="keywordsenglish",
            index=models.Index(fields=["token"], name="data_keywor_token_760957_idx"),
        ),
    ]