from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField


# Create your models here.

class Authors(models.Model):
    id = models.AutoField(primary_key=True)
    first_Name = models.CharField(max_length=200, unique=True)
    last_Name = models.CharField(max_length=200, unique=True)

class Books(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    author_id = models.IntegerField(unique=True)
    description = models.CharField(max_length=400)
    author_first_Name = models.CharField(max_length=200, unique=True)
    author_last_Name = models.CharField(max_length=200, unique=True)
    image_url = models.CharField(max_length=400)

class Businesses(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    address = models.CharField(max_length=400)
    image_url = models.CharField(max_length=400)
    owner_first_Name = models.CharField(max_length=200, unique=True)
    owner_last_Name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=600)

class BusinessOwners(models.Model):
    id = models.AutoField(primary_key=True)
    first_Name = models.CharField(max_length=200, unique=True)
    last_Name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=600)
    business_id = models.IntegerField(unique=True)

class FeaturedPerson(models.Model):
    id = models.AutoField(primary_key=True)
    first_Name = models.CharField(max_length=200, unique=True)
    last_Name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=600)
    website_link = models.CharField(max_length=200, unique=True)
