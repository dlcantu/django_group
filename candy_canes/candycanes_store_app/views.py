#logic and render pages
#backend uses models
#views page renders HTTP response
from django.shortcuts import render, redirect
from . import views
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to our store")

def checkout(request):
    return render(request, 'candycanes_store_app/templates/pages/checkout.html')

# Create your views here.
