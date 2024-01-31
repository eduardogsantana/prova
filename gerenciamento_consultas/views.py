from django.shortcuts import render, redirect
from .models import Consulta
from django.contrib import messages
from .forms import ConsultaForm

def index(request):
    consultas = Consulta.objects.all()
    return render(request, 'gerenciamento_consulta/index.html', {'consultas': consultas})

def register(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Consulta Marcada com Sucesso')
            form = ConsultaForm()
        else:
            messages.error(request, 'Erro ao marcar consulta')
    else:
        form = ConsultaForm

    return render(request, 'gerenciamento_consulta/register.html', {'form': form})

def delete_consulta(request, id):
    consulta_marcada = Consulta.objects.get(id=id)
    if request.method == 'POST':
        consulta_marcada.delete()
        return redirect('/')
    return render(request, 'gerenciamento_consulta/delete.html')