from django.contrib import admin
from music.models import Release, Track, ReleaseTrack, Label, Artist, Image

class ReleaseTracksInline(admin.StackedInline):
    model = ReleaseTrack
    extra = 0
    
class ReleaseImageInline(admin.StackedInline):
    model = Image
    extra = 0
    
class ReleaseAdmin(admin.ModelAdmin):
    inlines = [ReleaseTracksInline, ReleaseImageInline]
    list_display = ('title', 'artist_credit', 'catalog_number')
    
class TrackAdmin(admin.ModelAdmin):
    inlines = [ReleaseTracksInline,]

admin.site.register(Release, ReleaseAdmin)
admin.site.register(Track, TrackAdmin)
admin.site.register(Label)
admin.site.register(Artist)
