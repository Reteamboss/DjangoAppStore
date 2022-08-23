from django.urls import path
from .views import ProductListView, ShowDetail
from django.conf.urls import url
from catalog import views
from .views import ProductListView, ShowDetail

app_name = 'catalog'

urlpatterns = [
    path('<str:category_slug>/<slug:product_slug>/', ShowDetail.as_view(), name='product_detail',),
    url(r'^products/$', views.ProductListView.as_view(), name='products',),
    path('product/<slug:product_slug>/',views.ShowDetail.as_view(), name='product')
]
