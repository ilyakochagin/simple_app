# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class Profile(models.Model):
    """
    Class with information for every user, user and image
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        """
        Func for output username
        :return: username
        """
        return f'{self.user.username} Profile'

