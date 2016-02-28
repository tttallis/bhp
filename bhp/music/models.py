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
    release_date = models.DateField(null=True, blank=True)
    vague_date = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.title
        
class ReleaseTrack(models.Model):
    track = models.ForeignKey('Track')
    release = models.ForeignKey('Release')
    position = models.CharField(max_length=8, null=True, blank=True)
    
    def __unicode__(self):
        return "%s: %s" % (self.position, self.track)
        
class Track(models.Model):
    title = models.CharField(max_length=255)
    release = models.ManyToManyField('Release', through='ReleaseTrack')
    duration = models.CharField(max_length=8, null=True, blank=True)
    
    def __unicode__(self):
        return self.title