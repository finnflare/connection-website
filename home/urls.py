from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("mission", views.mission, name="mission"),
    path("team", views.team, name="team"),
    path("story", views.story, name="story"),
    path("faqs", views.faqs, name="faqs"),
    path("connect", views.connect, name="connect"),
]