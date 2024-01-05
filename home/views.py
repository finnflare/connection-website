from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "home/index.html")

def mission(request):
    return render(request, "home/mission.html")

def team(request):
    return render(request, "home/team.html")

def story(request):
    return render(request, "home/story.html")

def faqs(request):
    return render(request, "home/faqs.html")

def connect(request):
    return render(request, "home/connect.html")