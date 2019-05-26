# -*- coding: utf-8 -*-
import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from simple_app.forms import *
from simple_app.models import *
from teachers.models import *
from django.views.decorators.csrf import csrf_exempt


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


def home(request):
    """
    This func is main for homepage
    :param request:
    :return: render to /
    """
    context = get_context()

    context['title'] = 'Simple App'
    context['teachers'] = Teacher.objects.all().order_by('-teacher_median_rating')
    #context['tea_rait'] = Review.objects.filter()
    return render(request, 'home.html', context)


def about(request):
    """
    This func is main for about
    :param request:
    :return: render to about page
    """
    context = get_context()
    return render(request, 'about.html', context)


def all_complaints(request):
    """
    This func for output all complaints which is in database
    :param request:
    :return: render to page with all complaints
    """
    context = get_context()
    context['title'] = 'Simple App'
    context['complaints'] = Complaint.objects.all()
    return render(request, 'all_complaints.html', context)


def complaint(request):
    """
    This function add new complaint in database
    :param request:
    :return: new complaint
    """
    if request.method == 'POST':
        form = NewComplaint(request.POST)
        new_comp = Complaint(title=form.data['title'],
                             text=form.data['text'],
                             date=datetime.datetime.now(),
                             author_id=request.user.id,
                             author_name=request.user)
        new_comp.save()
        return redirect('home')

    context = get_context()
    context['title'] = u'Создание новой жалобы'
    context['form'] = NewComplaint()

    return render(request, 'complaint.html', context)


@csrf_exempt
def delete_complaint(request):
    print("adfsfdsf")
    """
    This function delete complaint by ajax request
    :param request:
    :return: delete complaint from database
    """
    if request.is_ajax():
        complaint_id = request.POST.get('id')
        print(complaint_id)
        Complaint.objects.filter(id=complaint_id).delete()
        return HttpResponse()


def my_complaints(request):
    context = get_context()
    context['complaints'] = Complaint.objects.all()
    return render(request, 'my_complaints.html', context)
