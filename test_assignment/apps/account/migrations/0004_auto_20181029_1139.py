# Generated by Django 2.1.2 on 2018-10-29 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_tweet_datetime_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='tweets_counter',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Tweet',
        ),
    ]
