from django.shortcuts import render
from django.http.response import HttpResponse
from.models import Products,ProductsCategory

# Create your views here.
def index(request):
    return render(request,'index.html')



def about(request):
    return render(request,'about.html')


def products(request):
    products = Products.objects.all().order_by("-id")
    context = {
        'products' : products

    }
    return render(request,'products.html',context)