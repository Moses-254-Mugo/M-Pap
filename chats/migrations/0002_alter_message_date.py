# Generated by Django 3.2.9 on 2021-11-04 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Date'),
        ),
    ]