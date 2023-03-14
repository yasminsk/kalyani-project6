from django.shortcuts import render

# Create your views here.
def jinja_print1(request):
    d={'name':'Rohit Sharma','age':35}
    return render(request,'jinja_print1.html',context=d)

def jinja_print2(request):
    d={'name':'Dhoni','age':40}
    return render(request,'jinja_print2.html',context=d)