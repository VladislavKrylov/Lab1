from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello world!", content_type="text/plain")


def home(request):
    return render(request, "templates/static_handler.html")
