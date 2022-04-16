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

			release.catalog_number = catalog_no
			release.cover_notes = r.data.get("notes", "")
			
			if r.data["year"]:
				release.release_date = date(r.year, 1, 1)
			artists = []
			for a in r.data["artists"]:
				artist, created = Artist.objects.get_or_create(
					name = a["name"],
				)
				artists.append(artist)
			release.artists.set(artists)
			
			for c in r.data["extraartists"]:
				artist, created = Artist.objects.get_or_create(
					name = c["name"],
				)
				role, created = Role.objects.get_or_create(
					artist=artist,
					release=release,
				)
				role.role=c["role"]
				role.tracks=c["tracks"]
				role.save()
			

			print('formats', r.formats)

			print('master', r.master)
			print('notes', r.notes)
#            print 'url', r.url
			print('videos', r.videos)
			print()
			print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
