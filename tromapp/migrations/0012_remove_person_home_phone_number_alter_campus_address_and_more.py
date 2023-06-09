# Generated by Django 4.1.6 on 2023-05-26 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tromapp', '0011_person_is_online'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='home_phone_number',
        ),
        migrations.AlterField(
            model_name='campus',
            name='address',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='campus',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cursus',
            name='title',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='employee',
            name='office',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='person',
            name='cellphone_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='person',
            name='password',
            field=models.CharField(max_length=10),
        ),
    ]
