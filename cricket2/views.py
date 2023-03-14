from django.shortcuts import render

# Create your views here.
def jinja_print3(request):
    d={'name':'Boomra','age':32}
    return render(request,'jinja_print3.html',context=d)

def jinja_print4(request):
    d={'name':'jadeja','age':37}
    return render(request,'jinja_print4.html',context=d)