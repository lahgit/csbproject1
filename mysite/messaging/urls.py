from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('private/<int:pk>', views.private, name='private'),
    path('private/<int:pk>/send', views.send, name='send'),
]