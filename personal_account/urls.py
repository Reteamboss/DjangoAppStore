from django.urls import path
from .views import personal_account_view
from django.conf.urls import url




urlpatterns = [

    path('', personal_account_view, name='personal_account'),


]
