# Generated by Django 2.0.7 on 2018-08-03 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_institution_reward'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=6),
        ),
    ]