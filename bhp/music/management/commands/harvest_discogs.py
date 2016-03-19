import discogs_client
from django.core.management.base import BaseCommand
from music.models import Release, Track, ReleaseTrack, Artist, Label
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
                catalog_number = catalog_no,
            )
            if r.year:
                release.release_date = date(r.year, 1, 1)
            artists = []
            for a in r.artists:
                artist, created = Artist.objects.get_or_create(
                    name = a.name,
                )
                artists.append(artist)
            release.artists.set(artists)
            
            

            print 'companies', r.companies
            print 'credits', r.credits
            print 'formats', r.formats
#             print 'id', r.id
            print 'images', r.images
            for i in r.images:
                image = urllib.urlretrieve(i['uri'])
#             self.poster_frame.save(os.path.basename(metadict.get('thumbnail_url')), File(open(result[0])))

            print 'master', r.master
            print 'notes', r.notes
            print 'status', r.status
            print 'styles', r.styles
            print 'thumb', r.thumb
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
