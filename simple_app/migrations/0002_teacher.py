# Generated by Django 2.1.5 on 2019-04-09 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('surname', models.TextField()),
                ('patronymic', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]