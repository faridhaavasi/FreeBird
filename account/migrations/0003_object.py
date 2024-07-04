# Generated by Django 5.0.6 on 2024-07-04 23:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('iFile', models.BooleanField(default=False, verbose_name='Is File')),
                ('iFolder', models.BooleanField(default=False, verbose_name='Is Folder')),
                ('size', models.CharField(max_length=50, verbose_name='Size')),
                ('path', models.TextField(verbose_name='Size')),
                ('trash', models.BooleanField(default=False, verbose_name='Is Trash')),
                ('stared', models.BooleanField(default=False, verbose_name='Is Stared')),
                ('shared', models.BooleanField(default=False, verbose_name='Is Shared')),
                ('sharedLink', models.CharField(blank=True, max_length=200, null=True, verbose_name='Shared Link')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
                ('sharedTo', models.ManyToManyField(related_name='sharedTo', to=settings.AUTH_USER_MODEL, verbose_name='Shared To')),
            ],
        ),
    ]
