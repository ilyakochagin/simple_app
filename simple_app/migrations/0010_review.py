# Generated by Django 2.1.5 on 2019-04-20 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_app', '0009_auto_20190414_0132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('teacher_id', models.IntegerField()),
                ('rating', models.IntegerField()),
            ],
        ),
    ]