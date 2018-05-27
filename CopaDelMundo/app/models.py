"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Team(models.Model):
    name=models.CharField(max_length=200,unique=True)
    user_admin=models.ForeignKey(User,on_delete=models.CASCADE, null=True)

class UserSettings(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    team=models.ForeignKey(Team, on_delete=models.SET_NULL,null=True)
    points=models.PositiveIntegerField(default=0)

class FootballTeam(models.Model):
    name=models.CharField(max_length=200,unique=True)


class Match(models.Model):
    home_team=models.ForeignKey(FootballTeam,related_name='home',on_delete=models.CASCADE)
    away_team=models.ForeignKey(FootballTeam,related_name='away',on_delete=models.CASCADE)
    home_goals=models.PositiveIntegerField(null=True)
    away_goals=models.PositiveIntegerField(null=True)
    home_odds=models.DecimalField(max_digits=5,decimal_places=2,null=True)
    away_odds=models.DecimalField(max_digits=5,decimal_places=2,null=True)
    home_points=models.PositiveIntegerField(null=True)
    away_points=models.PositiveIntegerField(null=True)
    date=models.DateTimeField(null=True)

class Pick(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    match=models.ForeignKey(Match,on_delete=models.CASCADE)
    home_picked=models.NullBooleanField()
