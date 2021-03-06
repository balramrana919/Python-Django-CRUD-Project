# Generated by Django 3.2.4 on 2021-07-15 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookDetailModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.IntegerField(max_length=10)),
                ('bookName', models.CharField(max_length=20)),
                ('bookAuthor', models.CharField(max_length=20)),
                ('bookPublication', models.CharField(max_length=50)),
                ('bookPublishDate', models.DateField()),
                ('bookGenre', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'bookdetail_db',
            },
        ),
        migrations.CreateModel(
            name='libraryuserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('L_ID', models.CharField(max_length=10)),
                ('fullname', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=30)),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'libraryuser_db',
            },
        ),
    ]
