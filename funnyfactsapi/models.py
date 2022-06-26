from django.db import models

# Create your models here.

class FunnyFacts(models.Model):
    day = models.CharField(max_length = 10, null=False)
    month = models.CharField(max_length = 10, null=False)
    fact = models.TextField(null=False)
    daymonth = models.SmallIntegerField(unique=True, null=False)