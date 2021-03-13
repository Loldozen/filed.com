from rest_framework import routers, serializers
from .models import Song, Podcast, AudioBook

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'name', 'duration', 'uploaded_time']
        #read_only_fields = ['id',]

class PodcastSerializer(serializers.ModelSerializer):

    participants = serializers.JSONField()
    class Meta:
        model = Podcast
        fields = ['id', 'participants', 'name', 'duration', 'uploaded_time', 
        'host']
        #read_only_fields = ['id',]

class AudioBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioBook
        fields = ['id', 'title', 'author', 'narrator', 'duration', 'uploaded_time']
        #read_only_fields = ['id',]