# Generated by Django 4.0.3 on 2022-05-25 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_remove_detail_email_remove_detail_pword_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='detail',
            name='pword',
            field=models.CharField(default='', max_length=100),
        ),
    ]
