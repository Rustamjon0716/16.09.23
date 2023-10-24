# Generated by Django 4.2.5 on 2023-09-15 10:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(default='', max_length=200)),
                ('author_lastname', models.CharField(default='', max_length=200)),
                ('author_birthday', models.DateTimeField(default=datetime.datetime.now)),
                ('author_status', models.CharField(default='', max_length=200)),
            ],
            options={
                'db_table': 'AuthorModel',
            },
        ),
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(default='', max_length=200)),
                ('book_page', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('description', models.TextField(default='write something!')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.authormodel')),
            ],
            options={
                'db_table': 'BookModel',
            },
        ),
    ]