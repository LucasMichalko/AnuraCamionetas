"""anuracamio URL Configuration

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

from anuracamio.view import index, Create_camionetas, ABM_Camionetas, Create_Objects, Stock_Camionetas, update_quantity

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index),
    path("Create_camionetas/", Create_camionetas),
    path("ABM_camionetas/", ABM_Camionetas),
    path("ABM_Productos/", Create_Objects),
    path("Stock_Camionetas/<int:ID_camio>", Stock_Camionetas),
    path('update_quantity/<int:product_id>/', update_quantity, name='update_quantity'),

]
