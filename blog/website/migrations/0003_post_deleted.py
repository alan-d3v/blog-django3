# Generated by Django 3.2.7 on 2021-09-20 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_post_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
