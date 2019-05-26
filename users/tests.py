# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test.client import Client
from .forms import UserRegisterForm, UserUpdateForm


class TestUsers(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.login(username='admin1', password='sudhsfdsdf', email='admin1@ya.ru')

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_logout_page(self):
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 200)

    def test_registration_form_invalid(self):
        invalid_data = {
            "username": "user3",
            "email": "user3@ya.ru",
            "password1": "secret",
            "password2": "not"
        }
        form = UserRegisterForm(data=invalid_data)
        form.is_valid()
        self.assertTrue(form.errors)

    def test_registration_form_valid(self):
        valid_data = {
            "username": "user3",
            "email": "user3@ya.ru",
            "password1": "secrettt",
            "password2": "secrettt"
        }
        form = UserRegisterForm(data=valid_data)
        form.is_valid()
        self.assertFalse(form.errors)

    def test_change_profile(self):
        invalid_data = {'email': 'dadadad'}
        form = UserUpdateForm(data=invalid_data)
        form.is_valid()
        self.assertTrue(form.errors)
        valid_data = {'email': 'asadd@ya.ru'}
        form = UserUpdateForm(data=valid_data)
        self.assertFalse(form.errors)
