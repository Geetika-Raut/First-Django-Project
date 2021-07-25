from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello World!")

def name1(request,naam):
    return HttpResponse(f"Welcome {naam}!")

def home(request):
    return HttpResponse("Welcome to home page!")

def scaler(request):
    return HttpResponse("Welcome to scaler page!")

def about(request):
    return HttpResponse("<h1> About Me </h1> <p> I am a budding web developer </p>")
