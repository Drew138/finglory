"""FinGlory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app import views as appViews
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', appViews.login, name='login'),
    path('home/', appViews.home, name='home'),
    path('gastos/', appViews.gastos, name='gastos'),
    path('ingresos/', appViews.ingresos, name='ingresos'),
    path('registrarGastos/', appViews.registrarGastosView, name='registrarGastos'),
    path('registrarUsuario/', appViews.registrarUsuarioView, name='registrarUsuario'),
    path('registrarIngresos/', appViews.registrarIngresosView,name='registrarIngresos'),
    #  path('borrarIngresos/', appViews.eliminar_ingresos),
    # path('borrarGastos/', appViews.eliminar_gastos) 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
