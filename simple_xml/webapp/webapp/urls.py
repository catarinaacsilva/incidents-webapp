"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from app import views
import os

urlpatterns = [
    path('', views.index),
    path('index_url', views.index),
    path('fogos_url', views.index),
    path('sobre_url', views.sobre),
    path('relatar_url', views.relatar),
    path('estatisticas_url', views.estatisticas),
    path('avisos_url', views.getRSS),
    path('getRSS2', views.getRSS2),
    path('store_url', views.store_data),
    path('listar_url', views.listar),
    path('confirm', views.confirm),
    path('notconfirm', views.notconfirm),
    path('listar_incidentes_map', views.list_recent_distance),
]

os.system('java -cp BaseX924.jar org.basex.BaseXServer &')