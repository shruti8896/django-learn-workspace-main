from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def home(request):
    redirect_path=reverse("home")
    

    return HttpResponseRedirect("/challenges/")