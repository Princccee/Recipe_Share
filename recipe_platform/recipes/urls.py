from django.urls import path
from . import views

urlpatterns = [
    path('regiter/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.register, name='logout'),

    path('recipes/', views.recipe_list, name='recipes'),
    path('recipes/create/', views.create_recipie, name='create_recipe'),
    path('recipes/<id:recipe_id>/', views.recipe_detail, name='recipe_detail'),
]