# Generated by Django 3.2.4 on 2021-06-24 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_review_platform'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]