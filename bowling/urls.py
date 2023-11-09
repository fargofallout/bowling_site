from django.urls import path

from . import views


app_name = "bowling"
urlpatterns = [
        path("", views.index, name="index"),
        path("bowler", views.bowler, name="bowler"),
        path("team", views.team, name="team"),
        path("create_bowler", views.create_bowler, name="create_bowler"),
        path("create_team", views.create_team, name="create_team"),
        path("league", views.league, name="league"),
        path("create_league", views.create_league, name="create_league"),
        path("week", views.week, name="week"),
        ]

