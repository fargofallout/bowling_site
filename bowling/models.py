from django.db import models
from django.db.models.deletion import DO_NOTHING


class Bowler(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    full_name = models.CharField(max_length=100, null=True)
    
    team = models.ForeignKey("Team", on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Team(models.Model):
    team_name = models.CharField(max_length=100, db_index=True)

    # models.Index("team_name", name="team_index")

    def __str__(self):
        return self.team_name


# I don't think there's a reason to split any of this up or make anything a datetime rather than a string
class League(models.Model):
    name = models.CharField(max_length=100)
    alley = models.CharField(max_length=100)
    season = models.CharField(max_length=20)
    day_of_week = models.CharField(max_length=20)
    league_complete = models.BooleanField(default=False)
    players_per_team = models.IntegerField(default=5)


class Week(models.Model):
    week_number = models.IntegerField()

    league = models.ForeignKey(League, on_delete=models.DO_NOTHING, null=True)


class HeadToHead(models.Model):
    series_complete = models.BooleanField(default=False)

    left_team = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name="left_team")
    right_team = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name="right_team")
    league = models.ForeignKey(League, on_delete=models.DO_NOTHING)
    week = models.ForeignKey(Week, on_delete=models.DO_NOTHING)


class TeamSeries(models.Model):
    lane = models.CharField(max_length=10, null=True)
    left_or_right = models.CharField(max_length=10, null=True)

    head_to_head = models.ForeignKey(HeadToHead, on_delete=models.DO_NOTHING, null=True)


class BowlerSeries(models.Model):
    position = models.IntegerField(default=1)
    handicap = models.IntegerField(default=0)
    no_handicap = models.BooleanField(default=False)

    team_series = models.ForeignKey(TeamSeries, on_delete=models.DO_NOTHING)


class Game(models.Model):
    score = models.IntegerField()
    game_number = models.IntegerField()
    robot_bowled = models.BooleanField(default=False)

    bowler = models.ForeignKey(Bowler, on_delete=models.DO_NOTHING)
    team = models.ForeignKey(Team, on_delete=models.DO_NOTHING)
    league = models.ForeignKey(League, on_delete=models.DO_NOTHING)
    week = models.ForeignKey(Week, on_delete=models.DO_NOTHING)
    bowler_series = models.ForeignKey(BowlerSeries, on_delete=DO_NOTHING, null=True)

