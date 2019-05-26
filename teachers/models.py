# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    """
    Class with model teacher in database
    """
    name = models.TextField()
    surname = models.TextField()
    patronymic = models.TextField()
    image = models.ImageField(upload_to='media/profile_pics')
    id = models.AutoField(primary_key=True)
    rating = models.FloatField(default=0.0)
    kol_reviews = models.IntegerField(default=0)
    kol_rating = models.IntegerField(default=0)
    teacher_median_rating = models.FloatField(default=0.0)
    teacher_obj = models.CharField(max_length=100)

class Review(models.Model):
    """
    Class with model review in database
    """
    text = models.TextField()
    teacher_id = models.IntegerField()
    author_name = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)


class Rating(models.Model):
    """
    Class with model rating in database
    """
    param1 = models.FloatField()
    param2 = models.FloatField()
    param3 = models.FloatField()
    rating = models.FloatField()
    teacher_id = models.IntegerField()
    author_name = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
