from django.db import models

# Create your models here.

class FunnyFacts(models.Model):
    day = models.SmallIntegerField(null=False)
    month = models.SmallIntegerField(null=False)
    fact = models.TextField(null=False)
    daymonth = models.SmallIntegerField(unique=True, null=False)