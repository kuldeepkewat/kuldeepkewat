
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dns_enumeration', views.dns_enumeration, name='dns_enumeration'),
]