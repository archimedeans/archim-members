from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('publications/', views.publications, name='publications'),
    path('documents/', views.documents, name='documents')
]