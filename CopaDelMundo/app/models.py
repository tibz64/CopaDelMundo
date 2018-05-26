"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Team(models.Model):
    name=models.CharField(max_length=200,unique=True)
    user_admin=models.ForeignKey(User,on_delete=models.CASCADE)

class UserSettings(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    team=models.ForeignKey(Team, on_delete=models.SET_NULL)
    points=models.IntegerField()

class FootballTeam(models.Model):
    name=models.CharField(max_length=200,unique=True)

class Match(models.Model):
    home_team=models.ForeignKey(FootballTeam,related_name='related_primary_footballteam',on_delete=models.CASCADE)
    away_team=models.ForeignKey(FootballTeam,related_name='related_secondary_footballteam',on_delete=models.CASCADE)
    home_goals=models.IntegerField()
    away_goals=models.IntegerField()
    home_odds=models.DecimalField()
    away_odds=models.DecimalField()
    home_points=models.IntegerField()
    away_points=models.IntegerField()
    date=models.DateTimeField()

class Pick(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    match=models.ForeignKey(Match,on_delete=models.CASCADE)
    home_picked=models.BooleanField()
