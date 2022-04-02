from __future__ import unicode_literals
from autoslug import AutoSlugField
from django.urls import reverse
from django.db import models
from urllib.parse import quote_plus
from embed_video.fields import EmbedVideoField

class Artist(models.Model):
    name = models.CharField(max_length=255)
    alpha_name = models.CharField(max_length=255, blank=True)    
    slug = AutoSlugField(populate_from='name')
    bio = models.TextField(blank=True)

    class Meta:
        ordering = ('alpha_name',)
    
    def get_absolute_url(self):
        return reverse('music:artist', kwargs={'slug': self.slug})

    def __unicode__(self):
        return self.name
        
    def proper_artist(self):
        return bool(self.releases.count())
        
    def __str__(self):
        return self.name
    

class Label(models.Model):
    name = models.CharField(max_length=255)
    long_name = models.CharField(max_length=255, blank=True)
    
    def __unicode__(self):
        return self.name
    
class Membership(models.Model):
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    start = models.DateTimeField(null=True, blank=True)
    finish = models.DateTimeField(null=True, blank=True)
    credit_name = models.CharField(max_length=255, blank=True)

class Person(models.Model):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255)
    
class Role(models.Model):
    artist = models.ForeignKey('Artist', related_name='role_artist', on_delete=models.CASCADE) 
    release = models.ForeignKey('Release', related_name='role_release', on_delete=models.CASCADE)
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
    label = models.ForeignKey('Label', on_delete=models.SET_NULL, null=True)
    artists = models.ManyToManyField('Artist', related_name='releases')
    _artist_credit = models.CharField(max_length=100, blank=True, help_text='Overrides artists')
    cover_image = models.ImageField(upload_to='covers', blank=True)
    credits = models.ManyToManyField('Artist', through='Role')
    cover_notes = models.TextField(blank=True)
    blurb = models.TextField(blank=True)
    
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
    track = models.ForeignKey('Track', on_delete=models.CASCADE)
    release = models.ForeignKey('Release', on_delete=models.CASCADE)
    position = models.CharField(max_length=8, null=True, blank=True)
    
    def __unicode__(self):
        return "%s: %s" % (self.position, self.track)
        
class Track(models.Model):
    title = models.CharField(max_length=255)
    release = models.ManyToManyField('Release', through='ReleaseTrack')
    duration = models.CharField(max_length=8, null=True, blank=True)
    blurb = models.TextField(blank=True)
    lyrics = models.TextField(blank=True)
    soundcloud = EmbedVideoField(blank=True)
    
    class Meta:
        ordering = ('title',)
    
    def __unicode__(self):
        return self.title
        
class Image(models.Model):
    image = models.ImageField(upload_to='imported_images')
    release = models.ForeignKey('Release', on_delete=models.CASCADE)

class Youtube(models.Model):
    url = EmbedVideoField()
    track = models.ForeignKey('Track', on_delete=models.CASCADE)
