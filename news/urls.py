from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('<slug:category_slug>/', views.news, name='news_by_category'),
    path('<slug:category_slug>/<slug:news_slug>/', views.news_detail, name='news_detail')
]