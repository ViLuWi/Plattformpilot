# Generated by Django 3.2.4 on 2021-06-09 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('platforms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='filter_functions',
            field=models.ManyToManyField(to='platforms.Functionality', verbose_name='Filtern nach'),
        ),
        migrations.AddField(
            model_name='category',
            name='related_category',
            field=models.ManyToManyField(blank=True, null=True, related_name='_core_category_related_category_+', to='core.Category'),
        ),
    ]
