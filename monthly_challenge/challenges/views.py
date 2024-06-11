from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect,Http404
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

monthly_challenge_dict={

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
    "december":None
}

def challenge(request):
    # list_items=""
    month_list=list(monthly_challenge_dict.keys())
    

    # for month in month_list:
    #     capitalized_month=month.capitalize()
    #     redirect_path=reverse("month-url",args=[month])
    #     list_items+=f"<li><a href=\"{redirect_path}\">{capitalized_month}</a></li>"
    #     print(type(list_items))

    #     response_data=f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)
    # print(month_list)
    return render(request,"challenges/index.html",{
        "month":month_list
    })

def monthly_chanllenge_number(request,month):
    try:
        months=list(monthly_challenge_dict.keys())
        month_name=months[month-1]
        redirect_path=reverse("month-url",args=[month_name])
        # print(redirect_path)
        return HttpResponseRedirect(redirect_path)
        # print("block worked")
        # return HttpResponseRedirect("/challenges/"+month_name)
    except:
        # resp_data=render_to_string("404.html")
        # return HttpResponseNotFound(resp_data )
        raise Http404()

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenge_dict[month.lower()]
    # if month == "january":
    #     challenge_text = "<h1>Drink 10 Glass of water everyday</h1>"
    # elif month == "feburary":
    #     challenge_text = "<h1>Walk for at least 20 minutes a day</h1>"
    # elif month == "march":
    #     challenge_text = "<h1>Read a book at least 45 min a day</h1>"
    # else:
    #     return HttpResponseNotFound("This months challenge will be displayed shortly")

        # render_to_string can be replaced with render directly instead of HttpResponse
        # return HttpResponse(render_to_string("challenges/challenge.html"))
        return render(request,"challenges/challenge.html",{
            "text":challenge_text,
            "month":month
        })
    except:
        return HttpResponseNotFound("<h1> This month is not supported</h1>")