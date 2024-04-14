from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('list-clients/', views.list_clients, name='list-clients'),
    path('list-clients/add-client/', views.add_client, name='add-client'),
    path('list-clients/<int:id>/', views.client_detail, name='client-detail'),
    path('list-clients/<int:id>/edit/', views.clients_edit, name='edit-client'),
    path('list-clients/<int:id>/delete/', views.clients_delete, name='delete-client'),

    # path('list-masters/', views.list_masters, name='list-masters'),
    # path('list-masters/add-masters/', views.add_masters, name='add-masters'),
    # path('list-masters/<int:id>/', views.masters_detail, name='masters-detail'),
    # path('list-masters/<int:id>/edit/', views.masters_edit, name='edit-masters'),
    # path('list-masters/<int:id>/delete/', views.masters_delete, name='delete-masters'),

]