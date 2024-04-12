from django.shortcuts import redirect, render
from .forms import ClientForm
from .models import Client

def list_clients(request):
    clients = Client.objects.all()
    context = {'clients':clients}
    return render(request,'list_clients.html', context)

def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-clients')
    else:
        form = ClientForm()

    context = {'form':form}

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

    context = {'form':form, 'id':id}
    return render(request,'edit_client.html', context)

def clients_delete(request, id):
    client = Client.objects.get(id=id)
    client.delete()
    return redirect('list-clients')