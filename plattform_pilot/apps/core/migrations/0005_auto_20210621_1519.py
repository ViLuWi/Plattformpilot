# Generated by Django 3.2.4 on 2021-06-21 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_category_related_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='suitable_for',
        ),
        migrations.AlterField(
            model_name='category',
            name='related_category',
            field=models.ManyToManyField(blank=True, null=True, related_name='_core_category_related_category_+', to='core.Category'),
        ),
    ]
