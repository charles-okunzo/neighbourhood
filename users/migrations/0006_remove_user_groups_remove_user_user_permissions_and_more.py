# Generated by Django 4.0.5 on 2022-06-18 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_user_neighbourhood'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
