from django.urls import path
from django.conf.urls import url
from catalog import views
from .views import ProductListView, ShowDetail

app_name = 'catalog'

urlpatterns = [
    path('<str:category_slug>/<slug:product_slug>/', ShowDetail.as_view(), name='product_detail',),
    path('<str:category_slug>/', ProductListView.as_view(), name='product_list_by_category',),
]
