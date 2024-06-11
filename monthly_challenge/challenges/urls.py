from django.urls import path

from . import views

urlpatterns=[

    # using placeholder segments to handle any url
    path("",views.challenge,name="index"),
    path("<int:month>",views.monthly_chanllenge_number),
    path("<str:month>",views.monthly_challenge,name="month-url")
]