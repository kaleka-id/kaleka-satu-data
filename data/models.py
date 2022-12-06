from django.contrib.gis.db import models
from django.contrib.auth.models import User

# Create your models here.
class Shop(models.Model):
    class Meta:
        verbose_name = 'Testing - Shop'
        verbose_name_plural = 'Testing - Shop'

    name = models.CharField(verbose_name='Shop Name', max_length=100)
    location = models.PointField()
    address = models.CharField(max_length=100)
    Open = models.BooleanField(verbose_name='Is the shop is open?')
    capacity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
