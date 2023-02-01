from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
import uuid

# PROFILE MODEL
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
  status = models.CharField(max_length=20, choices=[('Normal User', 'Normal User'), ('Observer', 'Observer')], default='Normal User')
  user_observed = models.ManyToManyField(User, blank=True, related_name='user_observed')

# PROFILE ADMIN
@admin.register(Profile)
class ProfileModel(admin.ModelAdmin):
  search_fields = ('user',)
  list_display = ('user', 'avatar', 'status')
  ordering = ('user',)
  filter_horizontal = ('user_observed',)