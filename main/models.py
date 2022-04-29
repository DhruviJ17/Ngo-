from sre_parse import CATEGORIES
from django.db import models
from login.models import *

# Create your models here.


# class VerifiedManager(models.Manager):
#     def get_queryset(self):
#         return super(PublishedManager, self).get_queryset().filter(ngo.is_verified=True)


class Requirements(models.Model):
    CATEGORIES= (
        ('M', 'Medicine'),
        ('F', 'Food'),
        ('C', 'Clothing'),
        ('S', 'Stationary')
    )

    ngo = models.ForeignKey(Ngo, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORIES, blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    
    def __str__(self):
        return self.name


class Donate(models.Model):
    requirements_name = models.ForeignKey(
        Requirements, null=True, blank=True, on_delete=models.CASCADE)
    ngo = models.ForeignKey(
        Ngo, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(
        Donor, null=True, blank=True, on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return str(self.requirements_name)
