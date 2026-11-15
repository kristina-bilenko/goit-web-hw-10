from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('author/<str:author_id>/', views.author_detail, name='author_detail'),
    path('add-author/', views.add_author, name='add_author'),
    path('add-quote/', views.add_quote, name='add_quote'),
    path("register/", views.register, name="register"),
    path("login/", views.user_login , name="login"),
    path('logout/', views.user_logout, name='logout'),
    path('add-author/', views.add_author, name='add_author'),
    path('add-quote/', views.add_quote, name='add_quote')
    ,
]