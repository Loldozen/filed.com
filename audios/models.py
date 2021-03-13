from django.db import models
from django.utils.translation import ugettext_lazy as _
from jsonfield import JSONField

# Create your models here.

class Song(models.Model):
    id = models.PositiveIntegerField(primary_key=True, unique=True)
    name = models.CharField(_("Name of the song"), max_length=100, blank=False, null=False)
    duration = models.PositiveIntegerField(_("Duration in seconds"))
    uploaded_time = models.DateTimeField(_("Upladed time"), auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

class Podcast(models.Model):
    id = models.PositiveIntegerField(primary_key=True, unique=True)
    name = models.CharField(_("Nameof the podcast"), max_length=100)
    duration = models.PositiveIntegerField(_("Duration in seconds"))
    uploaded_time = models.DateTimeField(_("Uploaded time and date"), auto_now_add=True)
    host = models.CharField(_("Host"), max_length=100)
    participants = JSONField()
    objects = models.Manager()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if len(self.participants) <= 10:
            super(Podcast, self).save(*args, **kwargs)

"""class Participant(models.Model):
    name = models.CharField(_("Name of participants"), max_length=100)
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE, related_name="participants")
"""
class AudioBook(models.Model):
    id = models.PositiveIntegerField(primary_key=True, unique=True)
    title = models.CharField(_("Title"), max_length=100)
    author = models.CharField(_("Author"), max_length=100)
    narrator = models.CharField(_("Narrator"), max_length=100)
    duration = models.PositiveIntegerField(_("Duration in seconds"))
    uploaded_time = models.DateTimeField(_("Uploaded time and date"), auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.title