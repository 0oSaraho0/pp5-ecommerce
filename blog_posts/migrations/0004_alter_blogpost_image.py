# Generated by Django 3.2 on 2022-10-26 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_posts', '0003_remove_blogpost_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, default='placeholder', null=True, upload_to=''),
        ),
    ]