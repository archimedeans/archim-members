from django.urls import path

from . import views

urlpatterns = [
    path('resources/', views.index, name='resources')
]