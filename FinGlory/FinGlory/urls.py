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
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', appViews.home, name='home'),
    path('gastos/', appViews.gastos, name='gastos'),
    path('ingresos/', appViews.ingresos, name='ingresos'),
    path('registrarGastos/', appViews.registrarGastosView, name='registrarGastos'),
    path('registrarIngresos/', appViews.registrarIngresosView,name='registrarIngresos'),
    path('estadisticas/', appViews.estadisticas, name='estadisticas'),
    path('actualizarIngresos/<pk>/', appViews.actualizarIngresosView, name = 'ingresos/actualizarIngresos'),
    path('eliminarIngresos/<pk>/', appViews.eliminarIngresosView, name = 'ingresos/eliminarIngresos'),
    path('actualizarGastos/<pk>/', appViews.actualizarGastosView, name = 'gastos/actualizarGastos'),
    path('eliminarGastos/<pk>/', appViews.eliminarGastosView, name = 'gastos/eliminarGastos'),

    path('', LoginView.as_view(template_name='inicio.html'), name='login'),
    path('registrarUsuario/', appViews.registrarUsuarioView, name='registrarUsuario'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
