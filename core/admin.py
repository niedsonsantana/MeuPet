from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
#from .forms import CustomUsuarioCreateForm, CustomUsuarioChangeForm
from .models import Animal #CustomUsuario

# Register your models here.

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ( '_autor', 'nome', 'porte', 'cor', 'castrado','tipo','image')
    exclude = ['autor',]

    def _autor(self, instance):
        return f'{instance.autor.get_full_name()}'

    def get_queryset(self, request):
        qs = super(AnimalAdmin, self).get_queryset(request)
        return qs.filter(autor=request.user)

    def save_model(self, request, obj, form, change):
        obj.autor = request.user
        super().save_model(request, obj, form, change)


#@admin.register(CustomUsuario)
# class CustomUsuarioAdmin(UserAdmin):
#     add_form = CustomUsuarioCreateForm
#     form = CustomUsuarioChangeForm
#     model = CustomUsuario
#     list_display = ('first_name', 'last_name', 'email', 'fone', 'is_staff')
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'fone')}),
#         ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#         ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
#     )