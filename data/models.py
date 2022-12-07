from django.contrib.gis.db import models
from django.contrib.auth.models import User

# Create your models here.
class Shop(models.Model):
    class Meta:
        verbose_name = 'Testing - Shop'
        verbose_name_plural = 'Testing - Shop'

    name_shop = models.CharField(verbose_name='Shop Name', max_length=100)
    geom = models.PointField(verbose_name='Location', null=True, blank=True)
    address = models.CharField(max_length=100)
    Open = models.BooleanField(verbose_name='Is the shop is open?')
    capacity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_shop

# REGISTER DATASET KE SINI -- agar bisa dibaca di User Permission
from .dataset.alamat import *
from .dataset.anggota_keluarga import *
from .dataset.isced_attainment import *
from .dataset.iucn import *
from .dataset.kbji import *
from .dataset.keluarga import *
from .dataset.kodepos import *
from .dataset.negara import *
from .dataset.orang import *
from .dataset.profesi import *
from .dataset.sitc import *
from .dataset.spesies import *
from .dataset.testing import *
