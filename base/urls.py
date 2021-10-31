from django.urls import path
from base import views

urlpatterns = [
    path('', views.ContactList.as_view(), name='contacts'),
    path('add-contact/', views.add_contact, name='add_contact'),
    path('edit-contact/<int:pk>/', views.edit_contact, name='edit_contact'),
    path('delete-contact/<int:pk>/', views.delete_contact, name='delete_contact'),
    path('search-contact/', views.search_contact, name='search_contact'),
]