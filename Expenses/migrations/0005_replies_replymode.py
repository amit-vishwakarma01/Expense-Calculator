# Generated by Django 4.1 on 2022-09-18 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Expenses', '0004_replies'),
    ]

    operations = [
        migrations.AddField(
            model_name='replies',
            name='replymode',
            field=models.CharField(default='', max_length=100),
        ),
    ]