from django.urls import path

from .api_views import (PersonListAPIView,
                        NewEntryAPIView,
                        DeleteAPIView,
                        EditAPIView)

urlpatterns = [
    path('address_book/', PersonListAPIView.as_view(), name='address_book'),
    path('delete/<int:id>/', DeleteAPIView.as_view(), name='delete_entry'),
    path('edit/<int:pk>/', EditAPIView.as_view(), name='edit_entry'),
    path('new_entry/', NewEntryAPIView.as_view(), name='new_entry'),
]
