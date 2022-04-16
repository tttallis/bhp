import discogs_client
from django.core.management.base import BaseCommand
from music.models import Release, Track, ReleaseTrack, Artist, Label, Role
from django.db import models
from datetime import date
from django.conf import settings
import urllib
from django.core.files import File
import os
from rich import inspect


class Command(BaseCommand):
    help = "Extract BHP discography data from discogs.com and store it locally."

    def handle(self, *args, **options):
        d = discogs_client.Client(
            "BigHomeProductionBot/0.1", user_token=settings.DISCOGS_TOKEN
        )
        l = d.label(settings.DISCOGS_LABEL_ID)
        label, created = Label.objects.get_or_create(
            name=l.name,  # who said I was pedantic?
        )
        for r in l.releases.page(1):  # paging - how do?

            inspect(r)
            catalog_no = r.data["catno"]
            release, created = Release.objects.get_or_create(
                title=r.data["title"],
                vague_date=True,
                label=label,
            )
            print(title)
            release.save()
