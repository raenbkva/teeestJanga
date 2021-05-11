from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('api/recipes/', views.RecipesView.as_view(), name='recipes'),
    path('api/dishes',views.DishesView.as_view(),name='dishes'),
    path('',views.index, name='main'),
]
