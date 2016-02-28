from django.contrib import admin
from music.models import Release, Track, ReleaseTrack

class ReleaseTracksInline(admin.StackedInline):
    model = ReleaseTrack
    extra = 0
    

class ReleaseAdmin(admin.ModelAdmin):
    inlines = [ReleaseTracksInline,]
    
class TrackAdmin(admin.ModelAdmin):
    inlines = [ReleaseTracksInline,]

admin.site.register(Release, ReleaseAdmin)
admin.site.register(Track, TrackAdmin)