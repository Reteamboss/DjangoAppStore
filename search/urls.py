from django.urls import path
from .views import ESearchView
from django.conf.urls import url


app_name = 'search'

urlpatterns = [
    url(r'^$', ESearchView.as_view(), name='index'),
]
