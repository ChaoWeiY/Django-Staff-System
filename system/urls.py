"""system URL Configuration

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
from django.contrib import admin
from django.urls import path, re_path
from Staff.views import *
from django.views.static import serve
from system import settings
urlpatterns = [
    path('admin/', admin.site.urls),  
    path('add_employee/', add_employee),
    path('list_employee/', list_employee),
    path('edit_employee/<int:emp_id>/', edit_employee),
    path('del_employee/<int:emp_id>/', delete_employee),
    path('add_dep/', add_dep),
    path('list_dep/', list_dep),
    path('del_dep/<int:dep_id>/', del_dep),
    path('edit_dep/<int:dep_id>/', edit_dep),
    path('add_group/', add_group),
    path('list_group/', list_group),
    path('del_group/<int:group_id>/', del_group),
    path('edit_group/<int:group_id>/', edit_group),    
    path('', index),
    re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
