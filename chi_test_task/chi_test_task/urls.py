"""chi_test_task URL Configuration

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

from address_book.views import new_entry, address_book, delete_entry, edit_entry, search_entry

urlpatterns = [
    path('admin/', admin.site.urls),
    path('address_book/', address_book, name='address_book'),
    path('new_entry/', new_entry, name='new_entry'),
    path('delete_entry/<int:index>/', delete_entry, name='delete_entry'),
    path('edit_entry/<int:id>/', edit_entry, name='edit_entry'),
    path('search_entry/', search_entry, name='search_entry'),
]
