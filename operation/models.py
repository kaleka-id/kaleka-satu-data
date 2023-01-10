from django.db import models
from django.contrib.postgres.fields import array, HStoreField
from django_better_admin_arrayfield.models.fields import ArrayField
from django.contrib.auth.models import User
import uuid

# FORMS
class Forms(models.Model):
  class Meta:
    verbose_name = 'Form'
    verbose_name_plural = 'Forms'

  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  nama = models.CharField(max_length=40, verbose_name='Nama Form')
  url_path = models.CharField(max_length=80, verbose_name='URL Path')
  url_add = models.CharField(max_length=80, verbose_name='URL Tambah Data')
  perms_view = models.CharField(max_length=80, verbose_name='View Permission')
  perms_add = models.CharField(max_length=80, verbose_name='Add Permission')

# DOCS
class Docs(models.Model):
  class Meta:
    verbose_name = 'Documentation'
    verbose_name_plural = 'Documentations'

  judul = models.CharField(max_length=40)
  gambar = models.FileField(upload_to='docs/')
  deskripsi = models.TextField()
  dictionary_data = HStoreField(blank=True, null=True, verbose_name='Dictionary')
  updated_at = models.DateTimeField(auto_now=True)

# DICTIONARY
class Dictionary(models.Model):
  class Meta:
    verbose_name_plural = 'Dictionaries'

  nama = models.CharField(max_length=40)
  url_path = models.CharField(max_length=80, verbose_name='URL Path')
  perms_view = models.CharField(max_length=80, verbose_name='View Permission')

# DASHBOARD
class Dashboard(models.Model):
  nama = models.CharField(max_length=40)
  category = models.CharField(max_length=20, choices=[('Static CSV', 'Static CSV'), ('Google Sheets', 'Google Sheets'), ('Google BigQuery', 'Google BigQuery'), ('Amazon Redshift', 'Amazon Redshift'), ('PostgreSQL Database', 'PostgreSQL Database'), ('MySQL Database', 'MySQL Database')])
  email_maintainer = models.CharField(max_length=40)
  page_url = models.CharField(max_length=80, verbose_name='Page URL Path')
  embed_url = models.URLField(max_length=100, verbose_name='Embed URL Path')
  width = models.CharField(max_length=8, help_text="Gunakan CSS unit seperti '%', 'cm', 'mm', 'in', 'px', 'pt', dan 'pc'. Contoh: 500px")
  height = models.CharField(max_length=8, help_text="Gunakan CSS unit seperti '%', 'cm', 'mm', 'in', 'px', 'pt', dan 'pc'. Contoh: 500px")
  perms_view = ArrayField(models.CharField(max_length=30), null=True, blank=True)

# CATALOG
class Catalog(models.Model):
  nama = models.CharField(max_length=40)
  email_maintainer = models.CharField(max_length=40)
  page_url = models.CharField(max_length=80, verbose_name='Page URL Path')
  embed_url = models.URLField(max_length=200, verbose_name='Embed URL Path')
  spreadsheet_url = models.URLField(max_length=200, verbose_name='Google Sheets URL Path')
  width = models.CharField(max_length=8, help_text="Gunakan CSS unit seperti '%', 'cm', 'mm', 'in', 'px', 'pt', dan 'pc'. Contoh: 500px")
  height = models.CharField(max_length=8, help_text="Gunakan CSS unit seperti '%', 'cm', 'mm', 'in', 'px', 'pt', dan 'pc'. Contoh: 500px")
  perms_view = ArrayField(models.CharField(max_length=30), null=True, blank=True)

# PROFILE
class Profile(models.Model):
  PATH = '/static/images/avatar/'
  AVATAR_CHOICES = [
    (PATH + 'brownbear.png', 'Brown Bear'),
    (PATH + 'bull.png', 'Bull'),
    (PATH + 'camel.png', 'Camel'),
    (PATH + 'capybara.png', 'Capybara'),
    (PATH + 'cat.png', 'Cat'),
    (PATH + 'chicken.png', 'Chicken'),
    (PATH + 'chimp.png', 'Chimp'),
    (PATH + 'cow.png', 'Cow'),
    (PATH + 'deer.png', 'Deer'),
    (PATH + 'dog.png', 'Dog'),
    (PATH + 'donkey.png', 'Donkey'),
    (PATH + 'duck.png', 'Duck'),
    (PATH + 'eagle.png', 'Eagle'),
    (PATH + 'elephant.png', 'Elephant'),
    (PATH + 'femaledeer.png', 'Female Deer'),
    (PATH + 'flamingo.png', 'Flamingo'),
    (PATH + 'fox.png', 'Fox'),
    (PATH + 'frog.png', 'Frog'),
    (PATH + 'giraffe.png', 'Giraffe'),
    (PATH + 'gorilla.png', 'Gorilla'),
    (PATH + 'hippo.png', 'Hippo'),
    (PATH + 'horse.png', 'Horse'),
    (PATH + 'kangaroo.png', 'Kangaroo'),
    (PATH + 'koala.png', 'Koala'),
    (PATH + 'lemur.png', 'Lemur'),
    (PATH + 'lion.png', 'Lion'),
    (PATH + 'llama.png', 'Llama'),
    (PATH + 'monkey.png', 'Monkey'),
    (PATH + 'mouse.png', 'Mouse'),
    (PATH + 'nutria.png', 'Nutria'),
    (PATH + 'otter.png', 'Otter'),
    (PATH + 'owl.png', 'Owl'),
    (PATH + 'panda.png', 'Panda'),
    (PATH + 'panther.png', 'Panther'),
    (PATH + 'penguin.png', 'Penguin'),
    (PATH + 'pig.png', 'Pig'),
    (PATH + 'prairiedog.png', 'Prairie Dog'),
    (PATH + 'rabbit.png', 'Rabbit'),
    (PATH + 'racoon.png', 'Racoon'),
    (PATH + 'redpanda.png', 'Redpanda'),
    (PATH + 'rhino.png', 'Rhino'),
    (PATH + 'seal.png', 'Seal'),
    (PATH + 'sheep.png', 'Sheep'),
    (PATH + 'sloth.png', 'Sloth'),
    (PATH + 'snake.png', 'Snake'),
    (PATH + 'tiger.png', 'Tiger'),
    (PATH + 'toucan.png', 'Toucan'),
    (PATH + 'turtle.png', 'Turtle'),
    (PATH + 'walrus.png', 'Walrus'),
    (PATH + 'whitebear.png', 'White Bear'),
    (PATH + 'wombat.png', 'Wombat'),
    (PATH + 'zebra.png', 'Zebra'),
  ]

  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  avatar = models.CharField(max_length=50, choices=AVATAR_CHOICES, default=PATH + 'chimp.png')