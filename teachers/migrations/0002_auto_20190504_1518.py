# Generated by Django 2.1.5 on 2019-05-04 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='kol_reviews',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='teacher',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.FloatField(default=5.0),
        ),
    ]
