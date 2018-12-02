#!C:/Python27/ArcGISx6410.2/python.exe
#-*- coding:utf-8 -*-
"""
#============================================
#
# Project: tango_with_django_project
# Name: The file name is urls
# Purpose: 
# Auther: changxiong
# Tel: 17372796660
#
#============================================
#
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
]