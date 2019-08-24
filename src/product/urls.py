from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<str:category_slug>', views.product_list, name='product_list_category'),
    path('detail/<str:product_slug>', views.product_detail, name='product_detail')
]