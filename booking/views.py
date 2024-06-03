from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import ServiceList


class ServiceList(generic.ListView):
    model = service_name