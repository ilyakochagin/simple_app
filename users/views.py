# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.shortcuts import render
from django.shortcuts import redirect
from teachers.models import *


def get_context():
    """
    Make context array
    :return: context
    """
    context = dict()
    kol_rating = 0
    kol_reviews = len(Review.objects.all())
    for teacher in Teacher.objects.all():
        kol_rating += teacher.kol_rating
    context['teachers'] = Teacher.objects.all()
    context['total_teachers'] = len(Teacher.objects.all())
    context['total_rating'] = kol_rating
    context['total_reviews'] = kol_reviews
    context['total_users'] = len(User.objects.all())
    most = Teacher.objects.first()
    if most is not None:
        for teacher in Teacher.objects.all():
            if most.kol_reviews < teacher.kol_reviews:
                most = teacher

        context['most_popular'] = most.id
    return context


def register(request):
    """
    Register form
    :param request:
    :return: add new user in database
    """
    form = None
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт создан {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    context = get_context()
    context['form'] = form
    context['title'] = 'Register'
    return render(request, 'register.html', context)


@login_required
def profile(request):
    """
    Change profile information
    :param request:
    :return: updated request.user profile
    """
    context = get_context()
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, u'Ваш аккаунт был обновлен!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        context['u_form'] = u_form
        context['p_form'] = p_form
    return render(request, 'profile.html', context)
