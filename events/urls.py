from django.urls import path

from . import views

urlpatterns = [
    path(r'events/', views.events, name='events'),
    path(r'events/<term>', views.events, name='events')
]