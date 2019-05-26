# -*- coding: utf-8 -*-
from django import forms
from django.forms.widgets import *
from django.forms.fields import *
from .models import Review
from teachers.last_teacher_id import last_teacher_id as lti

teacher_objects = (('WEB', 'WEB'),
                   ('C++', 'C++'),
                   ('Python', 'Python'),
                   ('Assembler', 'Assembler'),
                   ('Roboto', 'Roboto'),
                   (u'ЕГЭ', u'ЕГЭ'),
                   (u'ОГЭ', u'ОГЭ'),
                   (u'Видеомонтаж', u'Видеомонтаж'),
                   ('CTF', 'CTF'),
                   ('Delphi', 'Delphi'),
                   ('Olymp', 'Olymp'),
                   ('Linux', 'Linux'),
                   (u'Промышленное программирование', u'Промышленное программирование'),
                   ('3D', '3D'),
                   ('C#', 'C#'),
                   ('PHP', 'PHP'),
                   ('JavaScript', 'JavaScript'),
                   (u'Мобильная разработка', u'Мобильная разработка'))


class NewTeacher(forms.Form):
    """
    Class with form for add new teacher
    """
    surname = forms.CharField(label=u'Фамилия', max_length=100)
    name = forms.CharField(label=u'Имя', max_length=100)
    patronymic = forms.CharField(label=u'Отчество', max_length=100)
    image = forms.ImageField(label=u'Фото')
    obj = forms.MultipleChoiceField(label=u'Предметы учителя',
                                    required=False,
                                    widget=CheckboxSelectMultiple,
                                    choices=teacher_objects)


class NewReview(forms.Form):
    """
    Class with form to add new review
    """
    text = forms.CharField(label=u'Текст отзыва', widget=forms.Textarea)



class rating(forms.Field):
    """
    Class with form to change or add rating for teacher
    """
    first_param = forms.Field
    second_param = forms.Field
    third_param = forms.Field
