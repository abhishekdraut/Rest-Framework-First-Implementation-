# Generated by Django 3.2.7 on 2021-09-29 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
