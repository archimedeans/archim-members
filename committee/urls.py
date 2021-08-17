from django.urls import path

from . import views

urlpatterns = [
    path('committee/', views.index, name='committee')
]