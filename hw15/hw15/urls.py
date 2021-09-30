"""hw15 URL Configuration

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
from django.views.decorators.cache import cache_page

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books_list/', cache_page(5)(views.BooksListView.as_view()), name='books_list'),
    path('create_object/', views.CreateObjectView.as_view(), name='create_object'),
    path('edit_object/<int:pk>/', views.EditObjectView.as_view(), name='edit_object'),
    path('delete_object/<int:pk>/', views.DeleteObjectView.as_view(), name='delete_object'),
]
