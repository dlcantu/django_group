#logic and render pages
#backend uses models
#views page renders HTTP response
from django.shortcuts import render, redirect
from .models import Product
#from django.http import HttpResponse

def home(request):
    return render(request, 'pages/home.html')

def checkout(request):
    print("Checkout")
    return render(request, 'pages/checkout.html')

def list_home(request):
    home_list = Product.objects.all()  # gets all of the to do lists from the database and store them in a variable
  
    # creates the context dictionary to send the blog posts to the template
    context = {
       'home_list': home_list
    }
    return render(request, 'pages/home.html', context)

    

# Create your views here.
