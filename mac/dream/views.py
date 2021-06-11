from django.shortcuts import render
from django.http import  HttpResponse
from math import ceil
from .models import  product
# Create your views here.
def index(request):
    products=product.objects.all()
    n=len(products)
    nSlide =  n//3+ceil((n/3)-(n//3))
    prams={"no_of_Slide": nSlide, "product": products, "range": range(nSlide), "data": int (3),}

    return render(request, 'dream/index.html', prams)
def about(request):
    return render(request, 'dream/about.html')
def contact(request):
    return HttpResponse('hello contact')
def productview(request):
    return HttpResponse('hello productview')
def tracker(request):
    return HttpResponse('hello tracker')
def search(request):
    return HttpResponse('hello search')
def cheackout(request):
    return HttpResponse('hello cheackout')
