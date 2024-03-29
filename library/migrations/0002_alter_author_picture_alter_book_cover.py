# Generated by Django 4.2 on 2024-02-24 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='picture',
            field=models.ImageField(blank=True, default='', upload_to='pictures/authors/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, default='', upload_to='pictures/cover'),
        ),
    ]
