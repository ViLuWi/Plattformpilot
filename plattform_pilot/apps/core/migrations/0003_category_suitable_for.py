# Generated by Django 3.2.4 on 2021-06-21 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platforms', '0001_initial'),
        ('core', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='suitable_for',
            field=models.ManyToManyField(to='platforms.Suitable'),
        ),
    ]
