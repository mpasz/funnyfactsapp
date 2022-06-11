from django.db import models

# Create your models here.

class CallendarMonths(models.Model):
    month_name = models.CharField(max_length=15, null=False)

class FunnyFacts(models.Model):
    day = models.SmallIntegerField(null=False)
    month = models.SmallIntegerField(null=False)
    fact = models.TextField(null=False)
    daymonth = models.SmallIntegerField(unique=True, null=False)