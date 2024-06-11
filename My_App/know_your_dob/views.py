from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def DOB(request):
    return HttpResponse("<h1>Hello from know your dob page</h1>")
