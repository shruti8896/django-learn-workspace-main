from django.urls import path

from my_monthly_task import views


urlpatterns = [
    path("",views.month_list),
    path("<int:month>",views.my_monthly_task_number),
    path("<str:month>",views.my_monthly_task,name="month_url")
]
