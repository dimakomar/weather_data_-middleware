
from django.db import models
from decimal import Decimal


class Month(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    t_max = models.CharField(max_length = 10)
    t_min = models.CharField(max_length = 10)
    af_days = models.CharField(max_length = 10)
    rain_mm = models.CharField(max_length = 10)
    sun_hours = models.CharField(max_length = 10)

    def __init__(self, year, month, t_max, t_min, af_days, rain_mm, sun_hours):
        self.year = year
        self.month = month
        self.t_max = t_max
        self.t_min = t_min
        self.af_days = af_days
        self.rain_mm = rain_mm
        self.sun_hours = sun_hours

    def _asdict(self):
        return self.__dict__
