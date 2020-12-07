"""meuPet URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import meuPet.settings as settings
from django.conf.urls.static import static
from users.views import create_user
from django.urls import path, include
from core.views import IndexView, CreateAnimalView, UpdateAnimalView, DeleteAnimalView, PageUser

urlpatterns = [
                  path('', IndexView.as_view(), name='index'),
                  path('createuser/', create_user, name='create_user'),
                  path('accounts/', include('django.contrib.auth.urls'), name='entrar'),
                  path('add/', CreateAnimalView.as_view(), name='add_animal'),
                  path('<int:pk>/update/', UpdateAnimalView.as_view(), name='upd_animal'),
                  path('<int:pk>/delete/', DeleteAnimalView.as_view(), name='del_animal'),
                  path('<int:pk>/user', PageUser.as_view(), name='page_user')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
