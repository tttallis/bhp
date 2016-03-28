import discogs_client
from django.core.management.base import BaseCommand
from music.models import Release, Track, ReleaseTrack, Artist, Label, Role
from django.db import models
from datetime import date
from django.conf import settings
import urllib
from django.core.files import File
import os

class Command(BaseCommand):
    help = 'Extract BHP discography data from discogs.com and store it locally.'

    def handle(self, *args, **options):
        d = discogs_client.Client('BigHomeProductionBot/0.1', user_token=settings.DISCOGS_TOKEN)
        l = d.label(settings.DISCOGS_LABEL_ID)
        label, created = Label.objects.get_or_create(
            name = l.name, # who said I was pedantic?
        )
        for r in l.releases.page(1): # paging - how do?
            catalog_no = r.labels[0].catno
            release, created = Release.objects.get_or_create(
                title = r.title,
                vague_date = True,
                label = label,
            )
            release.catalog_number = catalog_no
            release.cover_notes = r.notes or ''
            
            if r.year:
                release.release_date = date(r.year, 1, 1)
            artists = []
            for a in r.artists:
                artist, created = Artist.objects.get_or_create(
                    name = a.name,
                )
                artists.append(artist)
            release.artists.set(artists)
            
            for c in r.credits:
                artist, created = Artist.objects.get_or_create(
                    name = c.name,
                )
                print artist
                Role.objects.create(
                    artist=artist,
                    release=release,
                )
                artist.role=c.role
                artist.tracks=c.tracks
                artist.save()
            

            print 'formats', r.formats

            print 'master', r.master
            print 'notes', r.notes
#            print 'url', r.url
            print 'videos', r.videos
            print
            print 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'



            release.save()
            for t in r.tracklist:
                track, created = Track.objects.get_or_create(
                    title = t.title,
                    defaults = {'duration': t.duration},
                )
                track.save()
                reltrack, created = ReleaseTrack.objects.get_or_create(
                    track = track,
                    release = release,
                    position = t.position,
                )
                reltrack.save()
                if t.artists:
                    print 'unstored track artists data', track, t.artists
                if t.credits:
                    print 'unstored track credits data', track, t.credits
