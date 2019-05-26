# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test.client import Client
from .models import Teacher, Review
from .forms import NewTeacher
from .views import get_context
from django.contrib.auth.models import User

class TeacherTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.username = 'admin1'
        self.client.login(username='admin1', password='sudhsfdsdf', email='admin1@ya.ru')
        User.objects.create(username='admin1', password='sudhsfdsdf', email='admin1@ya.ru')
        self.user = User.objects.get(id=1)
        Teacher.objects.create(name='abaca', surname='babac', patronymic='oaoaoo',
                      image='media/default.jpg', teacher_obj=['WEB', 'Python', 'C++'])
        Teacher.objects.create(name='abacaba', surname='babaca', patronymic='oaoaoo',
                               image='media/default.jpg', teacher_obj=['WEB', 'Assembler', 'C++'])
        Review.objects.create(text='sggg', teacher_id=2, author_name=self.user)
        Review.objects.create(text='sgggg', teacher_id=2, author_name=self.user)
        Review.objects.create(text='sggggg', teacher_id=1, author_name=self.user)
        Review.objects.create(text='sgggggg', teacher_id=2, author_name=self.user)
        Teacher.objects.filter(id=2).update(kol_reviews=3)
        Teacher.objects.filter(id=1).update(kol_reviews=1)

    def test_add_new_Teacher(self):
        Tch = Teacher.objects.get(id=1)
        self.assertEqual(Tch.name, 'abaca')
        self.assertEqual(Tch.surname, 'babac')
        self.assertEqual(Tch.patronymic, 'oaoaoo')

    def test_popular_Teacher1(self):
        tch = Teacher.objects.get(id=1)
        context = get_context()
        self.assertEqual(context['most_popular'], 1)

    def test_popular_Teacher2(self):
        tch1 = Teacher.objects.get(id=1)
        tch2 = Teacher.objects.get(id=2)
        context = get_context()
        #print(context['total_reviews'])
        #print(tch2.kol_reviews)
        self.assertEqual(context['most_popular'], 2)
