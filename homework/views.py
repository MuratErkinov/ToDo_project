from django.shortcuts import render, HttpResponse, redirect
from .models import ToMeet, Goal_for_month, Habits


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


def add_meeting(request):
    form = request.POST
    persone = form['todo_persone']
    phone_number = form['meeting_phone']
    date_of_meeting = form['meeting_date']
    comment = form['meeting_comment']
    tomeet = ToMeet(persone=persone, phone_number=phone_number, comment=comment, date_of_meeting=date_of_meeting)
    tomeet.save()
    return redirect(meeting)


def add_goal(request):
    form = request.POST
    goal = form['add_goal_text']
    month = form['add_goal_date']
    difficulty = form['add_goal_difficulty']
    reason_for_goal = form['add_goal_reason']
    goalForMonth = Goal_for_month(goal=goal, month=month, difficulty=difficulty, reason_for_goal=reason_for_goal)
    goalForMonth.save()
    return redirect(goal_for_month)


def habits(request):
    habits_list = Habits.objects.all()
    return render(request, 'habits.html', {'habits_list': habits_list})


def add_habits(request):
    form = request.POST
    name = form['habits_text']
    comment = form['habits_comment']
    habit = Habits(name=name, comment=comment)
    habit.save()
    return redirect(habits)


def delete_to_meet(request, id):
    tomeet = ToMeet.objects.get(id=id)
    tomeet.delete()
    return redirect(meeting)


def delete_goal(request, id):
    goalForMonth = Goal_for_month.objects.get(id=id)
    goalForMonth.delete()
    return redirect(goal_for_month)


def delete_habits(request, id):
    habit = Habits.objects.get(id=id)
    habit.delete()
    return redirect(habits)


def mark_to_meet(request, id):
    tomeet = ToMeet.objects.get(id=id)
    tomeet.is_favorite = True
    tomeet.save()
    return redirect(meeting)


def unmark_to_meet(request, id):
    tomeet = ToMeet.objects.get(id=id)
    tomeet.is_favorite = False
    tomeet.save()
    return redirect(meeting)


def mark_goal(request, id):
    goalForMonth = Goal_for_month.objects.get(id=id)
    goalForMonth.is_favorite = True
    goalForMonth.save()
    return redirect(goal_for_month)


def unmark_goal(request, id):
    goalForMonth = Goal_for_month.objects.get(id=id)
    goalForMonth.is_favorite = False
    goalForMonth.save()
    return redirect(goal_for_month)


def mark_habits(request, id):
    habit = Habits.objects.get(id=id)
    habit.important = True
    habit.save()
    return redirect(habits)


def unmark_habits(request, id):
    habit = Habits.objects.get(id=id)
    habit.important = False
    habit.save()
    return redirect(habits)
