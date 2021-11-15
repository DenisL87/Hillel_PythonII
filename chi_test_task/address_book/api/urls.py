from django.urls import path

from .api_views import (PersonListAPIView,
                        NewEntryAPIView,
                        EditAPIView,
                        DeleteAPIView)

urlpatterns = [
    path('address_book/', PersonListAPIView.as_view(), name='address_book'),
    path('new_entry/', NewEntryAPIView.as_view(), name='new_entry'),
    # path('search_entry', SearchAPIView.as_view(), name='search_entry'),
    path('edit_entry/', EditAPIView.as_view(), name='edit_entry'),
    path('delete_entry/<int:id>/', DeleteAPIView.as_view(), name='delete_entry'),
]
