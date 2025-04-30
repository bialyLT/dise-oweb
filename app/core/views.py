from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.models import Group



def home(request):
    return render(request, 'inicio/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            grupo = Group.objects.get(name='clientes')
            user.groups.add(grupo)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def productos(request):
    return render(request, 'productos/productos.html')

def servicios(request):
    return render(request, 'servicios/servicios.html')