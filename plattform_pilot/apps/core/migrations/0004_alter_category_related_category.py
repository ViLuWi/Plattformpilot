# Generated by Django 3.2.4 on 2021-06-21 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_category_suitable_for'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='related_category',
            field=models.ManyToManyField(related_name='_core_category_related_category_+', to='core.Category'),
        ),
    ]