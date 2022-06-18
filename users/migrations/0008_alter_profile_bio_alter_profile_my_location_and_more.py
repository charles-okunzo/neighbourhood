# Generated by Django 4.0.5 on 2022-06-18 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myhood_app', '0005_remove_user_groups_remove_user_user_permissions_and_more'),
        ('users', '0007_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='my_location',
            field=models.CharField(max_length=100, null=True, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='neighbourhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to='myhood_app.neighbourhood'),
        ),
    ]