#logic and render pages
#backend uses models
#views page renders HTTP response
from django.shortcuts import render, redirect
from .models import Product
#from django.views.decorators.csrf import csrf_exempt
#from django.http import HttpResponse

def home(request):
    home_list = Product.objects.all()  # gets all of the to do lists from the database and store them in a variable
    # creates the context dictionary to send the blog posts to the template
    context = {
       'home_list': home_list
    }
    return render(request, 'pages/home.html', context)
    
def purchase(request, id):
    if request.method == "GET":
        return render(request, 'pages/home.html')
    elif request.method == "POST":
        product = Product.objects.get(id=id)
        print(product)
    return redirect('home')

def checkout_item(request, id):
    print("THIS IS THE ID", id)
    product = Product.objects.get(id=id)
    if product.favorite == False:
        product.favorite = True
        messages.success(request, "Marked as fav!")
    else:
        product.favorite = False
    product.save()
    return redirect('all')

def checkout(request):
    print("Checkout")
    return render(request, 'pages/checkout.html')

def confirmation(request):
    print("Confirmation")
    return render(request, 'pages/confirmation.html')

#def list_home(request):
    #return render(request, 'pages/home.html', context)

    

# Create your views here.
