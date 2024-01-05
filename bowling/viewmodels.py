from .models import Bowler, Team, League


def create_bowler(first_name: str, last_name: str):
    new_bowler = Bowler(first_name=first_name, last_name=last_name, full_name=f"{first_name} {last_name}")
    new_bowler.save()


def modify_bowler(bowler_id: int, first_name: str = "", last_name: str = ""):
    # should I check to make sure the id exists here? or elsewhere?
    updated_bowler = Bowler.objects.get(pk=bowler_id)
    if first_name != "":
        updated_bowler.first_name = first_name

    if last_name != "":
        updated_bowler.last_name = last_name

    updated_bowler.save()


def delete_bowler(bowler_id: int):
    b = Bowler.objects.get(pk=bowler_id)
    b.delete()


def search_bowler(name: str) -> int:
    b = Bowler.objects.filter(first_name__contains=name) | Bowler.objects.filter(last_name__contains=name)
    return b


def create_team(team_name: str):
    t = Team(team_name=team_name)
    t.save()


def modify_team(team_id: int, new_name: str):
    updated_team = Team.objects.get(pk=team_id)
    updated_team.team_name = new_name
    updated_team.save()


def delete_team(team_id: int):
    t = Team.objects.get(pk=team_id)
    t.delete()


def search_team(name: str) -> int:
    t = Team.objects.filter(team_name__contains=name)
    return t


def create_league(name: str, alley: str, season: str, day_of_week: str, players_per_team: int):
    l = League(name=name, alley=alley, season=season, day_of_week=day_of_week, players_per_team=players_per_team)
    l.save()

