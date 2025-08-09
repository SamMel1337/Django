from django.shortcuts import render

# Create your views here.
def example_view(request):
    return render(request,"catalog/base.html")

def example(request):
    return render(request,"catalog/contacts.html")

def example1(request):
    return render(request,"catalog/home.html")



