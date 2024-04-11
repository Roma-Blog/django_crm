from django.urls import path
from . import views

urlpatterns = [
    path('list-clients/', views.list_clients),
]