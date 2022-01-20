# Generated by Django 2.2.14 on 2020-12-21 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
