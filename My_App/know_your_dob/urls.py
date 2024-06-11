from django.urls import path

from know_your_dob.views import DOB


urlpatterns = [
    path("",DOB)
]
