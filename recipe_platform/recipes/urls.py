from django.urls import path
from . import views

urlpatterns = [
    path('regiter/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.register, name='logout'),
]