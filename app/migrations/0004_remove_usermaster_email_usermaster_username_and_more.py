# Generated by Django 4.0.6 on 2022-08-03 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_usermaster_is_active_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermaster',
            name='email',
        ),
        migrations.AddField(
            model_name='usermaster',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='usermaster',
            name='contact',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='usermaster',
            name='firstname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='usermaster',
            name='lastname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='usermaster',
            name='password',
            field=models.CharField(default='', max_length=50),
        ),
    ]
