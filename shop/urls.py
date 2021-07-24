from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='shop_Home'),
    path('about/', views.about, name='shop_index'),
    path('contact/', views.contact, name='shop_index'),
    path('tracker/', views.tracker, name='shop_index'),
    path('checkout/', views.checkout, name='shop_index'),
    path('search/', views.search, name='shop_index'),
    path('products/<int:myid>', views.productview, name="Product_View")
]