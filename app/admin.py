from django.contrib import admin

# Register your models here.
from .models import Song, Podcast, Audiobook, PodcastParticipant

class SongAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ["pk",]


class PodcastAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ["pk",]


class AudiobookAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ["pk",]


class PodcastParticipantAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ["pk",]


admin.site.register(Song, SongAdmin)
admin.site.register(Podcast, PodcastAdmin)
admin.site.register(Audiobook, AudiobookAdmin)
admin.site.register(PodcastParticipant, PodcastParticipantAdmin)