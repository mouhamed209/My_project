# Generated by Django 4.1.6 on 2023-05-12 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tromapp', '0009_remove_invitation_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='publication_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
