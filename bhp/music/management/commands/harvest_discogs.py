import discogs_client
from django.core.management.base import BaseCommand
from music.models import Release, Track, ReleaseTrack
from django.db import models
from datetime import date


class Command(BaseCommand):
    help = 'Extract BHP discography data from discogs.com and store it locally.'

    def handle(self, *args, **options):
        d = discogs_client.Client('BigHomeProductionBot/0.1', user_token=TOKEN)
        label = d.label(BHP_LABEL_ID)
        for r in label.releases.page(1): # paging - how do?
            release, created = Release.objects.get_or_create(
                title = r.title,
                vague_date = True,
            )
            if r.year:
                release.release_date = date(r.year, 1, 1)
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