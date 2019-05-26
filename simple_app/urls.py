# -*- coding: utf-8 -*-
"""simple_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from simple_app import views
from django.contrib.auth import views as auth_views
from users import views as uviews
from teachers import views as tviews
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', uviews.register, name='register'),
    path('profile/', uviews.profile, name='profile'),
    path('complaint/', views.complaint, name='complaint'),
    path('all_complaints/', views.all_complaints, name='all_complaints'),
    path('new_teacher/', tviews.new_teacher, name='new_teacher'),
    path('teacher/delete', tviews.delete_teacher, name='delete_teacher'),
    path('teacher/<int:pk>/', tviews.teacher_view, name='teacher-detail'),
    path('review/<int:pk>', tviews.review, name='teacher-review'),
    path('complaint/delete', views.delete_complaint, name='delete_complaint'),
    path('rating/<int:pk>', tviews.teacher_rating, name='teacher_rating'),
    path('rating/change', tviews.rating_change, name='change_rating'),
    path('my_complaints/', views.my_complaints, name='my_complaints'),
    path('review/delete', tviews.review_delete, name='delete_review')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
