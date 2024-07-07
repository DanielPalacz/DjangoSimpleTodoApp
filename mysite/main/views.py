from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("<h1>Hello from index page.</h1>")


def v1(request):
    return HttpResponse("<h1>Hello from v1 page.</h1>")
