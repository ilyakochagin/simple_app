# Generated by Django 2.1.5 on 2019-04-11 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_app', '0006_auto_20190412_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(upload_to='media/profile_pics'),
        ),
    ]
