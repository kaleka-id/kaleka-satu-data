from django import forms
from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from django.contrib.gis.db import models
import uuid
from data.dataset.sitc import SITC
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.fields import HStoreField
from django_admin_hstore_widget.forms import HStoreFormField
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from django.contrib.auth.models import User

class Konsesi(models.Model):
  class Meta:
    verbose_name = 'Konsesi'
    verbose_name_plural = 'Konsesi'
    permissions = [
      ('search_lahanpoligon', 'Can search Konsesi in Dictionary')
    ]

  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  geom = models.PolygonField(verbose_name='Lahan')
  jenis_konsesi = models.CharField(max_length=40)
  komoditas = models.ForeignKey(SITC, on_delete=models.CASCADE)
  catatan_komoditas = models.TextField(null=True, blank=True)
  nomor_legal_konsesi = models.CharField(max_length=40)
  pemegang_konsesi = models.CharField(max_length=100)
  group_perusahaan = models.CharField(max_length=100, null=True, blank=True)
  tahun_konsesi = models.PositiveSmallIntegerField(validators=[MaxValueValidator(2100), MinValueValidator(1900)], default=1900)
  sertifikasi = HStoreField(blank=True, null=True, help_text='Diisi sesuai dengan sertifikasi yang berkaitan e.g. RSPO. Lihat dictionary terkait penamaan Key')
  status_data = models.CharField(max_length=20, choices=[('Updated', 'Updated'), ('Need Confirmation', 'Need Confirmation'), ('Not Valid', 'Not Valid')], default='Need Confirmation')
  keterangan = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

# KONSESI FORM
class KonsesiModelForm(forms.ModelForm):
  class Meta:
    model = Konsesi
    exclude = ()
  
  sertifikasi = HStoreFormField()

# KONSESI ADMIN
@admin.register(Konsesi)
class KonsesiModel(LeafletGeoAdmin, DynamicArrayMixin):
  search_fields = ('pemegang_konsesi', 'group_perusahaan')
  list_display = ('id', 'jenis_konsesi', 'pemegang_konsesi', 'komoditas', 'nomor_legal_konsesi')
  list_filter = ('jenis_konsesi', 'komoditas', 'nomor_legal_konsesi', 'pemegang_konsesi', 'group_perusahaan', 'tahun_konsesi', 'created_at', 'updated_at', 'user')
  readonly_fields = ('user',)
  raw_id_fields = ('komoditas',)

  form = KonsesiModelForm

  def save_model(self, request, obj, form, change): 
    obj.user = request.user
    obj.save()