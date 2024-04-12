from django.shortcuts import render,get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse


# Create your views here.
def cart_summary(request):
    return render(request, 'cart_summary.html',{})

def cart_add(request):
   #get the cart
   cart = Cart(request)
   #test for POSR
   if request.POST.get('action') == 'post':
       
       #get stuff
       product_id = int(request.POST.get('product_id'))

       #lookup product in db
       product = get_object_or_404(Product,id = product_id)

       #save the session
       cart.add(product=product)


       #retrurb response

       response = JsonResponse({ 'Product Name' : product.name })
       return response

def cart_update(request):
    pass

def cart_delete(request):
    pass