# Generated by Django 3.2 on 2022-10-20 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
