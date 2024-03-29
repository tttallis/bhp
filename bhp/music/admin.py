from django.contrib import admin
from music.models import (
    Release,
    Track,
    ReleaseTrack,
    Label,
    Artist,
    Image,
    Role,
    Youtube,
)
from embed_video.admin import AdminVideoMixin


class ReleaseTracksInline(admin.TabularInline):
    model = ReleaseTrack
    extra = 0


class ReleaseImageInline(admin.TabularInline):
    model = Image
    extra = 0


class ReleaseYoutubeInline(admin.TabularInline):
    model = Youtube
    extra = 0


class RoleInline(admin.TabularInline):
    model = Role
    extra = 0


class ReleaseAdmin(admin.ModelAdmin):
    inlines = [
        ReleaseTracksInline,
        ReleaseImageInline,
        RoleInline,
    ]
    list_display = ("title", "artist_credit", "catalog_number")


class TrackAdmin(AdminVideoMixin, admin.ModelAdmin):
    #     list_filter = ('artist',)
    list_display = ("title",)
    inlines = [
        ReleaseTracksInline,
        ReleaseYoutubeInline,
    ]


admin.site.register(Release, ReleaseAdmin)
admin.site.register(Track, TrackAdmin)
admin.site.register(Label)
admin.site.register(Artist)
