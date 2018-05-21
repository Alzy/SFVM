from django.db import models


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    approved = models.BooleanField(blank=True)
    approved_at = models.DateTimeField(blank=True, null=True)

    image = models.ImageField(width_field=500, height_field=500, blank=True)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    more_details_link = models.URLField(blank=True)

    def __str__(self):
        return self.name
