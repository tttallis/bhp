from __future__ import unicode_literals

from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=255)
    
class Membership(models.Model):
    artist = models.ForeignKey('Artist')
    person = models.ForeignKey('Person')
    start = models.DateTimeField(null=True, blank=True)
    finish = models.DateTimeField(null=True, blank=True)
    credit_name = models.CharField(max_length=255, blank=True)

class Person(models.Model):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255)    
    
class Release(models.Model):
    title = models.CharField(max_length=255)