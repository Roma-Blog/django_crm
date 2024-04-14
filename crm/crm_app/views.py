from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from .forms import ClientForm
from .models import Client

def list_clients(request):
    search = request.GET.get('search')
    if search:
        clients = Client.objects.filter(first_name__contains=search) | Client.objects.filter(last_name__contains=search)
    else:
        clients = Client.objects.all()
    paginator = Paginator(clients, 8)
    page_number = request.GET.get('page')
    page_objects = paginator.get_page(page_number)

    context = {'search':search, 'page_objects':page_objects}
    return render(request,'list_clients.html', context)

def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-clients')
    else:
        form = ClientForm()

    context = {'form':form, 'title':'Добавить клиента'}

    return render(request,'add_client.html', context)

def client_detail(request, id):
    client = Client.objects.get(id=id)
    context = {'client':client}
    return render(request,'client_detail.html', context)

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
    return render(request,'add_client.html', context)

def clients_delete(request, id):
    client = Client.objects.get(id=id)
    client.delete()
    return redirect('list-clients')

def index(request):
    return redirect('list-clients')