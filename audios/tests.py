from django.test import TestCase
from django.db.utils import IntegrityError
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Song, Podcast, AudioBook
from .serializers import SongSerializer,PodcastSerializer, AudioBookSerializer

# Create your tests here.
# Model tests
class SongTest(APITestCase):

    def setUp(self):
        self.song1 = Song.objects.create(id=1, name="ozymandias", duration=1234)
        self.create_song = 'http://127.0.0.1:8000/api/create/?file_type=song'
        self.update_song = 'http://127.0.0.1:8000/api/update/1/?file_type=song'
        self.delete_song = 'http://127.0.0.1:8000/api/delete/1/?file_type=song'
        self.list_song = 'http://127.0.0.1:8000/api/list/?file_type=song'
        self.read_song = 'http://127.0.0.1:8000/api/read/1/?file_type=song'


    def test_create_song(self):

        data = {
            "id": 2,
            "name": "believe",
            "duration": 1234
        }
        response = self.client.post(self.create_song, data, format='json') #Song.objects.create(id=2, name="Banuso", duration=-34950)
        self.assertEqual(Song.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_song_with_negative_duration(self):
        data = {
            "id": 3,
            "name": "believe",
            "duration": -1234
        }
        response = self.client.post(self.create_song, data, format='json')
        self.assertEqual(Song.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_song_with_no_id(self):
        data = {
            "id": '',
            "name": "believe",
            "duration": 50909
        }
        response = self.client.post(self.create_song, data, format='json')
        self.assertEqual(Song.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_song(self):
        data = {
            "id": 9,
            "name": "birthday",
            "duration": 2030
        }
        response = self.client.put(self.update_song, data, format='json')
        self.assertEqual(response.data['id'], 9)
        self.assertEqual(response.data['name'], 'birthday')
    
    def test_delete_song(self):
        response = self.client.delete(self.delete_song)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data, None)

class PodcastTest(APITestCase):

    def setUp(self):
        data = {
    "id": 33,
    "participants": [
        "mercy",
        "ahmad",
        "bobola",
        "dammy",
        "doctor",
        "Major lazer",
        "Alessia cara"
    ],
    "name": "hell and high water",
    "duration": 5000,
    "uploaded_time": "",
    "host": "major lazer"
}
        self.song1 = Podcast.objects.create(
    id= 33,
    participants= [
        "mercy",
        "ahmad",
        "bobola",
        "dammy",
        "doctor",
        "Major lazer",
        "Alessia cara"
    ],
    name ="hell and high water",
    duration= 5000,
    uploaded_time= "",
    host= "major lazer"
        )
        self.create_podcast = 'http://127.0.0.1:8000/api/create/?file_type=podcast'
        self.update_podcast = 'http://127.0.0.1:8000/api/update/33/?file_type=podcast'
        self.delete_podcast = 'http://127.0.0.1:8000/api/delete/33/?file_type=podcast'
        self.list_podcast = 'http://127.0.0.1:8000/api/list/?file_type=podcast'
        self.read_podcast = 'http://127.0.0.1:8000/api/read/33/?file_type=podcast'


    def test_create_podcast(self):

        data = {
    "id": 12,
    "participants": [
        "mercy",
        "ahmad",
        "bobola",
        "dammy",
        "doctor",
        "Billy ray cyrus",
        "closure"
    ],
    "name": "Old town road",
    "duration": 5000,
    "uploaded_time": "",
    "host": "lil nas x"
}
        response = self.client.post(self.create_podcast, data, format='json') #Song.objects.create(id=2, name="Banuso", duration=-34950)
        self.assertEqual(Song.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_song_with_more_than_10_participants(self):
        data = {
    "id": 22,
    "participants": [
        "mercy",
        "ahmad",
        "bobola",
        "dammy",
        "doctor",
        "Major lazer",
        "Alessia cara",
        "Billy ray cyrus",
        "Lil nas X",
        "cat stevens",
        "freddy mecury"
    ],
    "name": "AYyyy oooo",
    "duration": 5000,
    "uploaded_time": "",
    "host": "Queen"
}
        response = self.client.post(self.create_song, data, format='json')
        self.assertEqual(Song.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_song_with_no_id(self):
        data = {
    "id": '',
    "participants": [
        "mercy",
        "ahmad",
        "bobola",
        "dammy",
        "doctor",
        "Major lazer",
        "Alessia cara"
    ],
    "name": "hell and high water",
    "duration": 5000,
    "uploaded_time": "2021-03-09T09:28:45.756247Z",
    "host": "major lazer"
}
        response = self.client.post(self.create_podcast, data, format='json')
        self.assertEqual(Song.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_song(self):
        data = {
    "id": 33,
    "participants": [
        "mercy",
        "ahmad",
        "Sia",
        "Damola",
        "doctor",
        "Major lazer",
        "Alessia cara"
    ],
    "name": "Family",
    "duration": 5000,
    "uploaded_time": "",
    "host": "Lil nas X"
}
        response = self.client.put(self.update_song, data, format='json')
        self.assertEqual(response.data['id'], 33)
        self.assertEqual(response.data['name'], 'family')
    
    def test_delete_podcast(self):
        response = self.client.delete(self.delete_podcast)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data, None)