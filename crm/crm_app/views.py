from django.shortcuts import render

def list_clients(request): 
    return render(request,'list_clients.html')

def add_client(request):
    return render(request,'add_client.html')