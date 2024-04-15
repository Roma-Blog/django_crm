from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from .forms import ClientForm, ServiceForm
from .models import Client, Service


def index(request):
    return redirect('list-clients')

def list_clients(request):
    search = request.GET.get('search')
    if search:
        clients = Client.objects.filter(last_name__istartswith=search)| Client.objects.filter(first_name__istartswith=search) 
    else:
        clients = Client.objects.all()
    paginator = Paginator(clients, 8)
    page_number = request.GET.get('page')
    page_objects = paginator.get_page(page_number)

    context = {'search':search, 'page_objects':page_objects,}
    return render(request,'clients/list_clients.html', context)

def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-clients')
    else:
        form = ClientForm()

    context = {'form':form, 'title':'Добавить клиента'}

    return render(request,'form_object.html', context)

def client_detail(request, id):
    client = Client.objects.get(id=id)
    context = {'client':client}
    return render(request,'object_detail.html', context)

def clients_edit(request, id):
    client = Client.objects.get(id=id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client-detail', id)
    else:
        form = ClientForm(instance=client)

    context = {'form':form, 'id':id, 'title':'Редактировать информацию о клиенте'}
    return render(request,'form_object.html', context)

def clients_delete(request, id):
    client = Client.objects.get(id=id)
    client.delete()
    return redirect('list-clients')

def list_services(request):
    search = request.GET.get('search')
    if search:
        clients = Service.objects.filter(name_service__istartswith=search)
    else:
        clients = Service.objects.all()
    paginator = Paginator(clients, 8)
    page_number = request.GET.get('page')
    page_objects = paginator.get_page(page_number)
    context = {'search':search, 'page_objects':page_objects,}
    return render(request,'services/list_services.html', context)

def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-services')
    else:
        form = ServiceForm()

    context = {'form':form, 'title':'Добавить услугу'}

    return render(request,'form_object.html', context)

def service_edit(request, id):
    service = Service.objects.get(id=id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('list-services', id)
    else:
        form = ServiceForm(instance=service)

    context = {'form':form, 'id':id, 'title':'Редактировать информацию о услуге'}
    return render(request,'form_object.html', context)

def service_delete(request, id):
    service = Service.objects.get(id=id)
    service.delete()
    return redirect('list-services')