from django.db import models

# Create your models here.
class ActiveRecord(models.Model):
    resort_name = models.CharField(max_length=50)
    snow_overnight = models.FloatField(default=0, null=True)
    snow_24hrs = models.FloatField(default=0, null=True)
    snow_48hrs = models.FloatField(default=0, null=True)
    snow_72hrs = models.FloatField(default=0, null=True)
    snow_7days = models.FloatField(default=0, null=True)
    snow_30days = models.FloatField(default=0, null=True)
    snow_total = models.FloatField(default=0, null=True)
    snow_base_depth = models.FloatField(default=0, null=True)
    trails_total = models.IntegerField(default=0, null=True)
    trails_open = models.IntegerField(default=0, null=True)
    lifts_total = models.IntegerField(default=0, null=True)
    lifts_open = models.IntegerField(default=0, null=True)
    country = models.CharField(max_length=50, default='')
    region = models.CharField(max_length=50, default='')
    passes = models.CharField(max_length=50, default='')
    def __str__(self):
        return self.resort_name
