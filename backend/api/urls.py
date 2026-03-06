from django.urls import path
from . import views

urlpatterns = [
    path('health', views.health, name='health'),
    path('contact', views.contact, name='contact'),
    path('articles', views.articles_list, name='articles_list'),
    path('articles/<str:slug>', views.article_detail, name='article_detail'),
    path('statistics', views.statistics, name='statistics'),
    path('resume', views.resume, name='resume'),
]
