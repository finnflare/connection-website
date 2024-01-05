# Generated by Django 4.2.2 on 2023-07-13 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('time', models.DateTimeField(verbose_name='date contacted')),
                ('message', models.TextField()),
            ],
        ),
    ]
