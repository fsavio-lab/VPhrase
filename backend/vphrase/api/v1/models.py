from django.db import models
from ..utils import years_range
from django.core.validators import MaxValueValidator, MinValueValidator


class Movie(models.Model):
    """"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    year = models.IntegerField(("year"), choices=years_range)
    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        default=0.0    
    )
    votes = models.IntegerField(default=0)
    grossing_value = models.DecimalField(max_digits=15, decimal_places=2,default=0.0)

    def __str__(self):
        return self.name
