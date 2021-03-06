from django.db import models
from django.template.defaultfilters import slugify
from rest_framework import serializers


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, unique=True)

    approved = models.BooleanField(blank=True, default=False)
    approved_at = models.DateTimeField(blank=True, null=True, editable=False)

    image = models.ImageField(upload_to="flyers", blank=True)
    short_description = models.TextField(max_length=256, blank=True)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=64, blank=True)
    city = models.CharField(max_length=64, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    more_details_link = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
