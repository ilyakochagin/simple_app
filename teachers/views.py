# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from teachers.forms import *
from teachers.models import *
from django.views.decorators.csrf import csrf_exempt
from teachers.last_teacher_id import last_teacher_id as lti
from django.contrib import messages



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
            print(teacher.kol_reviews)
        context['most_popular'] = most.id
    return context


def teacher_view(request, pk):
    """
    This function used for output all information about each teacher
    :param request:
    :param pk:
    :return: render to page with address teacher/<int:pk>/
    """
    context = get_context()
    try:
        teacher = Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExist:
        return redirect('home')
    rev = Review.objects.all().reverse()
    context['teacher'] = teacher
    context['review'] = rev

    return render(request, 'teacher_detail.html', context)


def new_teacher(request):
    """
    This function add new teacher in database
    :param request:
    :return: form with fields for teacher
    """
    context = get_context()
    if request.method == 'POST':
        form = NewTeacher(request.POST, request.FILES)
        print(form.is_valid())
        print(form.errors)
        tch_obj = form.cleaned_data['obj']
        print(tch_obj[0])
        str_obj = ""
        for i in range(len(tch_obj)):
            str_obj += tch_obj[i]
            if i != len(tch_obj) - 1:
                str_obj += ", "
        if form.is_valid():
            new_tch = Teacher(name=form.cleaned_data['name'],
                                surname=form.cleaned_data['surname'],
                                patronymic=form.cleaned_data['patronymic'],
                                image=form.cleaned_data['image'],
                                teacher_obj=str_obj)
            new_tch.save()
            return redirect('home')
    context['form'] = NewTeacher()
    context['title'] = u'Добавление преподавателя'
    return render(request, 'new_teacher.html', context)


@csrf_exempt
def delete_teacher(request):
    """
    This function delete teacher by ajax request
    :param request:
    :return: Httpresponse
    """
    #print("aaaaaaaaa")
    if request.is_ajax():
        teacher_id = request.POST.get('id')
        print(teacher_id)
        Teacher.objects.filter(id=teacher_id).delete()
        Review.objects.filter(teacher_id=teacher_id).delete()
        return HttpResponse()


@csrf_exempt
def rating_change(request):
    #print('aaaaaaaaaaa')
    """
    This funcction change rating, consists of 3 parameters
    :param request:
    :return: httpresponse
    """
    if request.method == 'POST':
        rat = request.POST.get('rating')
        pr1 = request.POST.get('param1')
        pr2 = request.POST.get('param2')
        pr3 = request.POST.get('param3')
        teacher_id = request.POST.get('teacher_id')
        #print(pr1, pr2, pr3, rating)
        try:
            Rating.objects.get(teacher_id=teacher_id, author_name=request.user).delete()
            new_rait = Rating(param1=pr1,
                              param2=pr2,
                              param3=pr3,
                              rating=rat,
                              teacher_id=teacher_id,
                              author_name=request.user)
            new_rait.save()
        except Rating.DoesNotExist:
            new_rait = Rating(param1=pr1,
                              param2=pr2,
                              param3=pr3,
                              rating=rat,
                              teacher_id=teacher_id,
                              author_name=request.user)
            new_rait.save()
        rat = float(rat)
        rat += Teacher.objects.get(id=teacher_id).rating
        kol = Teacher.objects.get(id=teacher_id).kol_rating + 1
        Teacher.objects.filter(id=teacher_id).update(rating=rat)
        Teacher.objects.filter(id=teacher_id).update(kol_rating=kol)
        Teacher.objects.filter(id=teacher_id).update(teacher_median_rating=rat / kol)
        print('rating', Teacher.objects.get(id=teacher_id).rating)
        print('kol_rating', Teacher.objects.get(id=teacher_id).kol_rating)
        #print(Rating.objects.get(teacher_id=lti.last_t_id, author_name=request.user).rating)
        #Review.objects.get(teacher_id=lti.last_id, author_name=request.user).rating = rating
    return HttpResponse()


def review(request, pk):
    """
        This function add new review for teacher in database
        :param request:
        :param pk:
        :return: new review for teacher
    """
    if len(Review.objects.filter(teacher_id=pk, author_name=request.user)) > 0:
        messages.success(request, u'Вы уже оставили отзыв о данном преподавателе')
        return redirect('home')
    context = get_context()
    if request.method == 'POST':
        form = NewReview(request.POST)
        new_rev = Review(text=form.data['text'],
                          teacher_id=pk,
                          author_name=request.user)
        new_rev.save()
        kol_rev = Teacher.objects.get(id=pk).kol_reviews + 1
        Teacher.objects.filter(id=pk).update(kol_reviews=kol_rev)
        messages.success(request, u'Спасибо за ваш отзыв!')
        return redirect('home')

    #context['teacher_id'] = pk
    context['teacher'] = Teacher.objects.get(id=pk)
    context['form'] = NewReview()
    context['title'] = u'Добавление отзыва о преподавателе'
    return render(request, 'teacher-review.html', context)


def teacher_rating(request, pk):
    """
    This func answer for page with stars, when we change rating
    :param request:
    :return: render to rating/change
    """
    if len(Rating.objects.filter(teacher_id=pk, author_name=request.user)) == 0:
        #print('olololololo')
        context = get_context()
        context["image_stars"] = "/media/stars.png"
        return render(request, 'teacher_rating.html', context)
    messages.success(request, u'Вы уже поставили оценку этому учителю')
    return redirect('home')


@csrf_exempt
def review_delete(request):
    """
        This function delete teacher by ajax request
        :param request:
        :return: Httpresponse
        """
    # print("aaaaaaaaa")
    if request.is_ajax():
        review_id = request.POST.get('id')
        #print(teacher_id)
        pk = Review.objects.get(id=review_id).teacher_id
        Review.objects.filter(id=review_id).delete()
        kol_rev = Teacher.objects.get(id=pk).kol_reviews - 1
        Teacher.objects.filter(id=pk).update(kol_reviews=kol_rev)
        return HttpResponse()
