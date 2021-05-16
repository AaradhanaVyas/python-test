from django.db import models

# Create your models here.

AUDIO_FILE_TYPE = ['Song', 'Podcast', 'Audiobook']


class Song(models.Model):
    name = models.CharField(null=True, blank=True, max_length=100)
    duration = models.PositiveIntegerField(null=True, blank=True)
    uploaded_time = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    
    def __str__(self):
        return f"{self.pk}"

    class Meta:
        verbose_name = "Song"
        verbose_name_plural = "Songs"

    
class Podcast(models.Model):
    name = models.CharField(null=True, blank=True, max_length=100)
    duration = models.PositiveIntegerField(null=True, blank=True)
    uploaded_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,)
    host = models.CharField(null=True, blank=True, max_length=100)
    
    def __str__(self):
        return f"{self.pk}"

    class Meta:
        verbose_name = "Podcast"
        verbose_name_plural = "Podcasts"


class PodcastParticipant(models.Model):
    participant = models.CharField(null=True, blank=True, max_length=100)
    podcast = models.ForeignKey("Podcast", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.pk}"

    class Meta:
        verbose_name = "Podcast Participant"
        verbose_name_plural = "Podcast Participants"


class Audiobook(models.Model):
    title = models.CharField(null=True, blank=True, max_length=100)
    author = models.CharField(null=True, blank=True, max_length=100)
    narrator = models.CharField(null=True, blank=True, max_length=100)
    duration = models.PositiveIntegerField(null=True, blank=True)
    uploaded_time = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    
    def __str__(self):
        return f"{self.pk}"

    class Meta:
        verbose_name = "Audiobook"
        verbose_name_plural = "Audiobooks"