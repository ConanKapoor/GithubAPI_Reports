# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Idx', models.PositiveIntegerField()),
                ('User_name', models.CharField(max_length=200)),
                ('Full_name', models.CharField(blank=True, max_length=250, null=True)),
                ('Location', models.CharField(max_length=200)),
                ('Blog', models.CharField(max_length=200)),
                ('Public_repos', models.PositiveIntegerField()),
                ('Public_gists', models.PositiveIntegerField()),
                ('Email', models.CharField(blank=True, max_length=250, null=True)),
                ('Followers', models.PositiveIntegerField()),
                ('Following', models.PositiveIntegerField()),
                ('Updated_on', models.DateField()),
            ],
            options={
                'verbose_name': '1_User Data',
                'verbose_name_plural': '1_User Data',
            },
        ),
    ]
