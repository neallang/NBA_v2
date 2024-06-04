from django.db import models

class Player(models.Model):
    player_id = models.IntegerField(unique=True)
    full_name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    position = models.CharField(max_length=10)
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    college = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    draft_year = models.IntegerField(null=True, blank=True)
    draft_round = models.IntegerField(null=True, blank=True)
    draft_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.full_name