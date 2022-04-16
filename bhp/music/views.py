from django.shortcuts import render, get_object_or_404
from music.models import Artist, Release


def home(request):
    return render(request, "home.html")


def artists(request):
    personnel = Artist.objects.all()
    artists = personnel.filter(releases__isnull=False)
    return render(request, "music/artists.html", {"artists": artists})


def artist(request, slug):
    artist = get_object_or_404(Artist, slug=slug)
    return render(request, "music/artist.html", {"artist": artist})


def releases(request):
    releases = Release.objects.all()
    return render(request, "music/releases.html", {"releases": releases})


def release(request, slug):
    release = get_object_or_404(Release, slug=slug)
    return render(request, "music/release.html", {"release": release})
