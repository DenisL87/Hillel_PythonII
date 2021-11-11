from django.urls import path

from .api_views import PersonListAPIView

urlpatterns = [
    path('address_book/', PersonListAPIView.as_view(), name='address_book')
]