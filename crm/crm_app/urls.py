from django.urls import path
from . import views

urlpatterns = [
    path('list-clients/', views.list_clients),
    path('list-clients/add-client/', views.add_client),
]