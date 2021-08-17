from django.urls import path

from . import views

urlpatterns = [
    path('committee/', views.index, name='committee'),
    path('past-committee/', views.past, name='past-committee')
]