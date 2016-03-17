from __future__ import unicode_literals

from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.name

class Label(models.Model):
    name = models.CharField(max_length=255)
    long_name = models.CharField(max_length=255, blank=True)
    
    def __unicode__(self):
        return self.name
    
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
    catalog_number = models.CharField(max_length=100, blank=True)
    label = models.ForeignKey('Label')
    artists = models.ManyToManyField('Artist')
    _artist_credit = models.CharField(max_length=100, blank=True, help_text='Overrides artists')
    
    def __unicode__(self):
        return self.title
        
    @property
    def artist_credit(self):
        return self._artist_credit or ', '.join([artist.name for artist in self.artists.all()])
        
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
        
class Image(models.Model):
    image = models.ImageField(upload_to='imported_images')
    release = models.ForeignKey('Release')