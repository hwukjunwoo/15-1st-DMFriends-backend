# Generated by Django 3.1.4 on 2020-12-18 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20201217_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='board',
            name='content',
            field=models.CharField(max_length=150),
        ),
    ]
