from django.test import Client, TestCase
from django.urls import reverse
from .models import AUDIO_FILE_TYPE

class SongAudioFileTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_invalid_file_type(self):
        data = {
            "audioFileType": "test",
            "audioFileMetadata": {
                "name": "Song name",
                "duration": 34

            }
        }
        message = f"Invalid file type! Please select from {AUDIO_FILE_TYPE}"
        response = self.client.post(reverse("add-audio-file"), data)
        response_message = response.json()["message"]
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_message, message)


    def test_without_file_types(self):
        data = {
            "audioFileMetadata": {
                "name": "Song name",
                "duration": 34

            }
        }
        message = "audioFileType and audioFileMetadata are required!"
        response = self.client.post(reverse("add-audio-file"), data)
        response_message = response.json()["message"]
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_message, message)


    def test_without_name(self):
        data = {
            "audioFileType": "Song",
            "audioFileMetadata": {
                "duration": 34

            }
        }
        message = "Please resolve error(s) OR fill Missing field(s)!"
        response = self.client.post(reverse("add-audio-file"), data)
        response_message = response.json()["message"]
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_message, message)


    def test_audiobook_with_song_data(self):
        data = {
            "audioFileType": "Audiobook",
            "audioFileMetadata": {
                "name": "test UPDATED",
                "duration": 34
            }
        }
        message = "Please resolve error(s) OR fill Missing field(s)!"
        response = self.client.post(reverse("add-audio-file"), data)
        response_message = response.json()["data"]
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_message, message)


    def test_podcast_without_host(self):
        data = {
            "audioFileType": "Podcast",
            "audioFileMetadata": {
                "name": "test UPDATED",
                "duration": 34
            }
        }
        message = "Please resolve error(s) OR fill Missing field(s)!"
        response = self.client.post(reverse("add-audio-file"), data)
        response_message = response.json()["data"]
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_message, message)
