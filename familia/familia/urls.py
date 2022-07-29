"""familia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from familia.views import template_familia
from appFamily.views import create_family, all_family

urlpatterns = [
    path('admin/', admin.site.urls),
    path('template_familia/', template_familia, name = 'template_familia'),
    path('create_family/', create_family, name='create_family'),
    path('all_family/', all_family, name = 'all_family')
]
