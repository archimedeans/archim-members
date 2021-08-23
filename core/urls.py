from django.urls import path, re_path

from . import views

urlpatterns = [
    # path('', views.index, name='home'),
    re_path(r"^(?:index\.html)?$", views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('publications/', views.publications, name='publications'),
    path('documents/', views.documents, name='documents')
]