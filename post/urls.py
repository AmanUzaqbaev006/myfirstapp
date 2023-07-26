
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('home/<slug:slug>/', views.homeDetail, name='home_detail'),
    path('authors', views.AuthorPage, name='authors'),
    path('home/<slug:slug>/add-comment', views.add_comment, name='add-comment'),

    path('addPost/', views.addPost, name='addPost'),

    path('search/', views.searchBar, name='search'),]
