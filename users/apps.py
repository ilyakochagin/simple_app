# -*- coding: utf-8 -*-
from django.apps import AppConfig


class UsersConfig(AppConfig):
    """
    Class written for settings.py
    """
    name = 'users'
    def ready(self):
        import users.signals