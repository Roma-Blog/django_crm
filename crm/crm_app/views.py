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
            return redirect('/list-clients/')
    else:
        form = ClientForm()

    context = {'form':form}

    return render(request,'add_client.html', context)

def client_detail(request, id):
    client = Client.objects.get(id=id)
    context = {'client':client}
    return render(request,'client_detail.html', context)