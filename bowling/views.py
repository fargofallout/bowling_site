from django.shortcuts import HttpResponse, HttpResponseRedirect, render, reverse
from django.views.decorators.http import require_http_methods

from .models import Bowler, Team, League
import bowling.viewmodels as vm


# Create your views here.
def index(request):
    return render(request, "bowling/index.html")


@require_http_methods(["GET",])
def bowler(request):
    all_bowlers = Bowler.objects.order_by("first_name")
    bowlers = {"all_bowlers": all_bowlers}
    return render(request, "bowling/bowler.html", bowlers)


@require_http_methods(["POST",])
def create_bowler(request):
    r = request.POST
    vm.create_bowler(first_name=r["first_name"], last_name=r["last_name"])
    return HttpResponseRedirect(reverse("bowling:bowler"))


def team(request):
    all_teams = Team.objects.order_by("team_name")
    teams = {"all_teams": all_teams}
    return render(request, "bowling/team.html", teams)


# this would make sense to utilize htmx, right? because I don't want to replace the whole page - just part of it
@require_http_methods(["POST",])
def create_team(request):
    r = request.POST
    team_name = r["team_name"]
    if vm.search_team(team_name):
        error_message = "That team name already exists. Please use a different name."
        all_teams = Team.objects.order_by("team_name")
        teams = {"all_teams": all_teams, "error_message": error_message}
        return render(request, "bowling/team.html", teams)
    vm.create_team(r["team_name"])
    return HttpResponseRedirect(reverse("bowling:team"))


def league(request):
    all_leagues = League.objects.order_by("name")
    leagues = {"all_leagues": all_leagues}
    return render(request, "bowling/league.html", leagues)


@require_http_methods(["POST",])
def create_league(request):
    r = request.POST
    name = r["name"]
    alley = r["alley"]
    season = r["season"]
    day_of_week = r["day_of_week"]
    players_per_team = r["players_per_team"]

    vm.create_league(name=name, alley=alley, season=season, day_of_week=day_of_week, players_per_team=players_per_team)
    return HttpResponseRedirect(reverse("bowling:league"))



def week(request):
    all_teams = Team.objects.order_by("team_name")
    teams = {"all_teams": all_teams}
    return render(request, "bowling/week.html", teams)

