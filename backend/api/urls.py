from django.urls import path
from . import views

urlpatterns = [
    # Function-based views
    path('color/', views.color_view, name='color'),
    path('calculator/', views.calculator_view, name='calculator'),
] 