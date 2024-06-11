from django.http import HttpResponse
from django.shortcuts import render


def home_view(Request):
    print("This is home view")
    return render(Request,"home.html",{})
