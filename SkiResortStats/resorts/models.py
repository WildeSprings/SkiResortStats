from django.db import models

# Create your models here.
class ActiveRecord(models.Model):
    resort_name = models.CharField(max_length=50)
    snow_overnight = models.IntegerField(default=0)
    snow_24hrs = models.IntegerField(default=0)
    snow_48hrs = models.IntegerField(default=0)
    snow_72hrs = models.IntegerField(default=0)
    snow_7days = models.IntegerField(default=0)
    snow_30days = models.IntegerField(default=0)
    snow_total = models.IntegerField(default=0)
    snow_base_depth = models.IntegerField(default=0)
    trails_total = models.IntegerField(default=0)
    trails_open = models.IntegerField(default=0)
    lifts_total = models.IntegerField(default=0)
    lifts_open = models.IntegerField(default=0)
    def __str__(self):
        return self.resort_name
