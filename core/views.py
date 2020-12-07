from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Animal


class IndexView(ListView):
    paginate_by = 6
    ordering = 'id'
    models = Animal
    template_name = 'index.html'
    queryset = Animal.objects.all()
    context_object_name = 'animais'


class CreateAnimalView(LoginRequiredMixin, CreateView):
    login_url = ''
    model = Animal
    template_name = 'animal_form.html'
    fields = ['nome', 'porte', 'cor', 'castrado', 'tipo', 'cidade', 'image', 'info']
    success_url = reverse_lazy('index')

    def form_valid(self, form) :
        form.instance.usuario = self.request.user
        form.instance.email = self.request.user.email
        form.instance.fone = self.request.user.fone
        return super().form_valid(form)


class UpdateAnimalView(LoginRequiredMixin, UpdateView):
    model = Animal
    template_name = 'animal_update.html'
    fields = ['nome', 'porte', 'cor', 'castrado', 'tipo', 'image', 'info']

    def get_success_url(self):
        return reverse_lazy('page_user',  kwargs={'pk': self.request.user.pk})

    def form_invalid(self, form):
        form.instance.usuario_novo = self.request.user
        form.instance.usuario = True
        return super().form_valid(form)


class DeleteAnimalView(LoginRequiredMixin, DeleteView):
    model = Animal
    template_name = 'animal_del.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        return reverse_lazy('page_user',  kwargs={'pk': self.request.user.pk})


class PageUser(LoginRequiredMixin, ListView):
    paginate_by = 6
    ordering = 'id'
    models = Animal
    template_name = 'user_page.html'
    queryset = Animal.objects.all()
    context_object_name = 'animais'

    def get_queryset(self) :
        self.object_list = Animal.objects.filter(usuario=self.request.user)
        return self.object_list
