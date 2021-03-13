from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework import status, mixins, generics
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework.generics import get_object_or_404

from .serializers import PodcastSerializer, SongSerializer, AudioBookSerializer
from .models import AudioBook, Podcast, Song

# Create your views here.
@api_view(['GET', 'POST'])
def api_root(request, format=None):
    return Response({
        'create': reverse('create-file', request=request, format=format),
        'list': reverse('list-files', request=request, format=format),
        #'read': reverse('read-file', request=request, format=format),
        #'update': reverse('update-file', request=request, format=format),
        #'delete': reverse('delete-file', request=request, format=format),
    })

class AudioServer(generics.ListCreateAPIView):
    def get_file_type(self, *args, **kwargs):
        """if self.request.query_params["file_type"] :
            file_type = self.request.query_params["file_type"]
            return file_type
        else:
            return status.HTTP_400_BAD_REQUEST"""
        try:
            file_type = self.request.query_params["file_type"]
            return file_type
        except MultiValueDictKeyError:
            return (Response(status=status.HTTP_400_BAD_REQUEST))
        

    def get_serializer_class(self):
        file_type = self.get_file_type()
        if file_type == "song":
            return SongSerializer
        elif file_type == "podcast":
            return PodcastSerializer
        elif file_type == "audiobook":
            return AudioBookSerializer
        else:
            return (Response(status=status.HTTP_400_BAD_REQUEST))
        
    def get_queryset(self):
        file_type = self.get_file_type()
        if file_type == "song":
            return Song.objects.all()
        elif file_type == "audiobook":
            return AudioBook.objects.all()
        elif file_type == "podcast" :          
            return Podcast.objects.all()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class CreateAPI(AudioServer):

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ListFiles(AudioServer):
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class FileDetails(generics.RetrieveUpdateDestroyAPIView):

    def get_file_type(self, *args, **kwargs):

        try:
            file_type = self.request.query_params["file_type"]
            return file_type
        except MultiValueDictKeyError:
            return (Response(status=status.HTTP_400_BAD_REQUEST))

    def get_queryset(self):
        file_type = self.get_file_type()
        if file_type == "song":
            return get_object_or_404(Song, id=self.kwargs['pk'])
        elif file_type == "audiobook":
            return get_object_or_404(AudioBook, id=self.kwargs['pk'])
        elif file_type == "podcast" :         
            return get_object_or_404(Podcast, id=self.kwargs['pk'])
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def get_object(self):
        file_type = self.get_file_type()
        if file_type == "song":
            return get_object_or_404(Song, id=self.kwargs['pk'])        
        elif file_type == "audiobook":
            return get_object_or_404(AudioBook, id=self.kwargs['pk']) 
        elif file_type == "podcast" :          
            return  get_object_or_404(Podcast, id=self.kwargs['pk']) 
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        file_type = self.get_file_type()
        if file_type == "song":
            return SongSerializer
        elif file_type == "podcast":
            return PodcastSerializer
        elif file_type == "audiobook":
            return AudioBookSerializer
        else:
            return (Response(status=status.HTTP_400_BAD_REQUEST))


class ReadFile(FileDetails):

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class UpdateFile(FileDetails):

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class DeleteFile(FileDetails):
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)