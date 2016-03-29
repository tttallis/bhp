from __future__ import unicode_literals
from autoslug import AutoSlugField
from django.core.urlresolvers import reverse
from django.db import models
from urllib import quote_plus

class Artist(models.Model):
    name = models.CharField(max_length=255)
    alpha_name = models.CharField(max_length=255, blank=True)    
    slug = AutoSlugField(populate_from='name')
    bio = models.TextField(blank=True)
    class Meta:
        ordering = ('name',)
    
    def get_absolute_url(self):
        return reverse('music:artist', kwargs={'slug': self.slug})

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
    
class Role(models.Model):
    artist = models.ForeignKey('Artist', related_name='role_artist') 
    release = models.ForeignKey('Release', related_name='role_release')
    role = models.CharField(max_length=255, blank=True)
    tracks = models.CharField(max_length=255, blank=True)
    
    def __unicode__(self):
        return "%s: %s" % (self.artist, self.role)
    
class Release(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title')
    release_date = models.DateField(null=True, blank=True)
    vague_date = models.BooleanField(default=False)
    catalog_number = models.CharField(max_length=100, blank=True)
    label = models.ForeignKey('Label')
    artists = models.ManyToManyField('Artist', related_name='release_artist')
    _artist_credit = models.CharField(max_length=100, blank=True, help_text='Overrides artists')
    cover_image = models.ImageField(upload_to='covers', blank=True)
    credits = models.ManyToManyField('Artist', through='Role')
    cover_notes = models.TextField(blank=True)
    
    class Meta:
        ordering = ('-release_date',)
        
    def quote_plus_title(self):
        return quote_plus(self.title)
    
    def __unicode__(self):
        return self.title
        
    @property
    def artist_credit(self):
        return self._artist_credit or ', '.join([artist.name for artist in self.artists.all()])
        
    def get_absolute_url(self):
        return reverse('music:release', kwargs={'slug': self.slug})

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
    blurb = models.TextField(blank=True)
    lyrics = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.title
        
class Image(models.Model):
    image = models.ImageField(upload_to='imported_images')
    release = models.ForeignKey('Release')

class Youtube(models.Model):
    url = models.URLField()
    track = models.ForeignKey('Track')
