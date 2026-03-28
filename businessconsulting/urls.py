# urls.py
from django.urls import path
from .views import create_contact, get_contacts

urlpatterns = [
    path('contact/create/', create_contact, name='create_contact'),
    path('contact/list/', get_contacts, name='get_contacts'),
]