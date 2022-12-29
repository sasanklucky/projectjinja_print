from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d={'name':'sasank','age':22}
    return render(request,'jinja_print.html',d)


def jinja_print1(request):
     d={'name':'sasank','age':22,'mobile':[1234,2345]}
     return render(request,'jinja_print1.html',d)