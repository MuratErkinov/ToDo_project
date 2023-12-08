from django.shortcuts import render, HttpResponse
from .models import ToMeet, Goal_for_month


def homework(request):
    return render(request, 'homework.html')


def hw_2(request):
    return HttpResponse('Добро пожаловать в приложение ToDo - Admin) ')


def meeting(request):
    tomeet_list = ToMeet.objects.all()
    return render(request, 'meeting.html', {'tomeet_list': tomeet_list})


def goal_for_month(request):
    goal_for_month_list = Goal_for_month.objects.all()
    return render(request, 'goal_for_month.html', {'goal_for_month_list': goal_for_month_list})
