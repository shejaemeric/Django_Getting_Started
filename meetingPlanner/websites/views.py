from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def welcome(request):
    """greeting view function"""

    return HttpResponse("<h1>This is a greeting from django</h1>")
