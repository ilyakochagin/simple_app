# Generated by Django 2.1.5 on 2019-04-27 17:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('teacher_id', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('author_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('name', models.TextField()),
                ('surname', models.TextField()),
                ('patronymic', models.TextField()),
                ('image', models.ImageField(upload_to='media/profile_pics')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
