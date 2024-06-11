from sys import argv
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# dictionay to store all the month name and tasks

my_month_dict={
    "january":"Drink 10 Glass of water everyday",
    "feburary":"Walk for at least 20 minutes a day",
    "march":"Read a book at least 45 min a day",
    "april":"Workout 1 hour everyday ",
    "may":"Smile everyday",
    "june":"Drink more water",
    "july":"meditate for 20 minutes",
    "august":"Wake up at 4am in the morning",
    "september":"Go to bed at 10pm in the eveining",
    "october":"Help the needies",
    "november":"Focus on gaining a new skill every week",
    "december":"have no sugar for a month"
}


# Create your views here.
def month_list(request):
    months_list=list(my_month_dict.keys())
    return render(request, "my_monthly_task/index.html", {
        "month_list": months_list
    })

def my_monthly_task(request, month):
    try:
        my_task = my_month_dict[month.lower()]
        return render(request, "my_monthly_task/challenge.html", {
            "task": my_task,
            "challenge_month": month
        })
    except:
        return HttpResponse("<h1>Month not supported by us</h1>")

def my_monthly_task_number(request,month):
    try:
        print(month)
        months_list=list(my_month_dict.keys())
        month_name=months_list[month-1]
        redirected_path=reverse("month_url", args=[month_name])

        return HttpResponseRedirect(redirected_path)
    except:
        raise Http404()

    # return HttpResponse("<h1>hello from monthly challenge page of this project</h1>")
