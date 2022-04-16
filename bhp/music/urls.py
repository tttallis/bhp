"""bhp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django_distill import distill_re_path
from music import views
from music.models import Artist, Release

app_name = "music"


def get_index():
    return None


def get_all_artists():
    return list(Artist.objects.values_list("slug", flat=True))


def get_all_releases():
    return list(Release.objects.values_list("slug", flat=True))


urlpatterns = [
    #     re_path(r'^/$', views.home, name='home'),
    distill_re_path(
        r"^artists/$", views.artists, name="artists", distill_func=get_index
    ),
    distill_re_path(
        r"^artists/(?P<slug>[\w-]+)/$",
        views.artist,
        name="artist",
        distill_func=get_all_artists,
    ),
    distill_re_path(
        r"^releases/$", views.releases, name="releases", distill_func=get_index
    ),
    distill_re_path(
        r"^releases/(?P<slug>[\w-]+)/$",
        views.release,
        name="release",
        distill_func=get_all_releases,
    ),
]
