# Generated by Django 2.2.8 on 2019-12-16 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blogpage_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='user',
        ),
    ]