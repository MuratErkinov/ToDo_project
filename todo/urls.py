"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import *
from django.conf import settings
from django.conf.urls.static import static
from homework.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", homepage, name="home"),
    path("test/", test, name="test"),
    path("test2/", second),
    path("add-todo/", add_todo, name="add-todo"),
    path("delete-todo/<id>/", delete_todo, name="delete-todo"),
    path("mark-todo/<id>/", mark_todo, name="mark-todo"),
    path("unmark-todo/<id>/", unmark_todo, name="unmark-todo"),
    path('homework/', homework, name='homework'),
    path('hw/', hw_2, name='hw'),
    path('meeting/', meeting, name='meeting'),
    path('add-meeting/', add_meeting, name='add-meeting'),
    path('delete-to-meet/<id>/', delete_to_meet, name='delete-to-meet'),
    path('mark-to-meet/<id>/', mark_to_meet, name='mark-to-meet'),
    path('unmark-to-meet/<id>/', unmark_to_meet, name='unmark-to-meet'),
    path('goal_for_month/', goal_for_month, name='goal_for_month'),
    path('add-goal/', add_goal, name='add-goal'),
    path('delete-goal/<id>/', delete_goal, name='delete-goal'),
    path('mark-goal/<id>/', mark_goal, name='mark-goal'),
    path('unmark-goal/<id>/', unmark_goal, name='unmark-goal'),
    path('habits/', habits, name='habits'),
    path('add-habits/', add_habits, name='add-habits'),
    path('delete-habits/<id>/', delete_habits, name='delete-habits'),
    path('mark-habits/<id>/', mark_habits, name='mark-habits'),
    path('unmark-habits/<id>/', unmark_habits, name='unmark-habits'),
]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
