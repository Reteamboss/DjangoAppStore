from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import url

from .views import contact_view, success_view

urlpatterns = [

    url('support/', success_view, name='success'),
    path('', contact_view, name='support')
]
