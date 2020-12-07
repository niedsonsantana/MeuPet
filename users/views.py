from users.forms import CustomUsuarioCreateForm
#from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.



def create_user(request):
    if str(request.user) == 'AnonymousUser':
        if str(request.method) == 'POST':
            form = CustomUsuarioCreateForm(request.POST)
            if form.is_valid():
                form.save()
                form = CustomUsuarioCreateForm()

                messages.success(request, "cadastro salvo com sucesso")
            else:
               messages.error(request, "erro ao adcionar Pessoa")
        else:
            form = CustomUsuarioCreateForm()
        context = {
            'form': form
        }
        return render(request, 'usuario.html', context)
    else:
        return redirect('index')