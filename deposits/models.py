from django.db import models


class Deposit(models.Model):

    deposit = models.IntegerField()
    term = models.IntegerField()
    rate = models.FloatField(max_length=4)
    interest = models.IntegerField()
