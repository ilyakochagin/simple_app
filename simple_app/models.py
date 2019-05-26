# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Complaint(models.Model):
    """
        This is class in database with complaint
    """
    title = models.TextField()
    text = models.TextField()
    date = models.DateTimeField()
    author_id = models.IntegerField()
    author_name = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    id = models.AutoField(primary_key=True)
