# Generated by Django 3.1.7 on 2021-03-07 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', height_field='400', upload_to='profile_images', width_field='400'),
        ),
    ]
