from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recommend/', views.recommend, name='recommend'),
    path('recommend/recommend_cloths', views.recommend_clothing_items, name='recommend_cloths'),
    path('contact/', views.contact, name='contact'),
]