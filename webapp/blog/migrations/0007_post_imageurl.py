# Generated by Django 3.1.7 on 2021-04-12 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imageUrl',
            field=models.URLField(blank=True, max_length=400),
        ),
    ]