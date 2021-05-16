from rest_framework import response
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SongSerializer, PodcastSerializer, AudiobookSerializer, PodcastDetailSerializer
from rest_framework import status
from .models import AUDIO_FILE_TYPE, Song, Audiobook, Podcast
from python_test.helpers import serialized_response

class AudioFileAPIView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            if 'audioFileType' not in request.data or 'audioFileMetadata' not in request.data:
                message = "audioFileType and audioFileMetadata are required!"
                return Response({
                    'status' : False,
                    'message': message
                }, status=status.HTTP_400_BAD_REQUEST)

            if request.data['audioFileType'] not in AUDIO_FILE_TYPE:
                message = f"Invalid file type! Please select from {AUDIO_FILE_TYPE}"
                return Response({
                    'status' : False,
                    'message': message
                }, status=status.HTTP_400_BAD_REQUEST)

            message = "Audio file added successfully!"

            if request.data['audioFileType'] == AUDIO_FILE_TYPE[0]:
                serializer = SongSerializer(data=request.data['audioFileMetadata'], context={"request": request})
            
            if request.data['audioFileType'] == AUDIO_FILE_TYPE[1]:
                serializer = PodcastSerializer(data=request.data['audioFileMetadata'], context={"request": request})

            if request.data['audioFileType'] == AUDIO_FILE_TYPE[2]:
                serializer = AudiobookSerializer(data=request.data['audioFileMetadata'], context={"request": request})

            response_status, result, message = serialized_response(serializer, message)
            status_code = status.HTTP_201_CREATED if response_status else status.HTTP_400_BAD_REQUEST
            return Response({
                'status' : response_status,
                'message': message,
                'data': result
            }, status = status_code)


        except Exception as inst:
            message = str(inst)
            return Response({
                    'status' : False,
                    'message': message
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def get(self, request, file_type, pk):
        try:
            if file_type not in AUDIO_FILE_TYPE:
                message = f"Invalid file type- {file_type}! Select from {AUDIO_FILE_TYPE}"
                return Response({
                            'status' : False,
                            'message': message
                        }, status=status.HTTP_404_NOT_FOUND)

            if file_type == AUDIO_FILE_TYPE[0]:
                song = Song.objects.get(pk=pk)
                serializer = SongSerializer(song, context={"request": request})

            if file_type == AUDIO_FILE_TYPE[1]:
                podcast = Podcast.objects.get(pk=pk)
                serializer = PodcastDetailSerializer(podcast, context={"request": request})

            if file_type == AUDIO_FILE_TYPE[2]:
                audiobook = Audiobook.objects.get(pk=pk)
                serializer = AudiobookSerializer(audiobook, context={"request": request})

            message = "Audio file fetched Successfully!"
            return Response({
                        'status' : True,
                        'message' : message,
                        'data': serializer.data

                    }, status=status.HTTP_200_OK)
        except Exception as inst:
            message = str(inst)
            return Response({
                    'status' : False,
                    'message': message
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def delete(self, request, file_type, pk):
        try:
            if file_type not in AUDIO_FILE_TYPE:
                message = f"Invalid file type- {file_type}! Select from {AUDIO_FILE_TYPE}"
                return Response({
                            'status' : False,
                            'message': message
                        }, status=status.HTTP_404_NOT_FOUND)

            if file_type == AUDIO_FILE_TYPE[0]:
                Song.objects.get(pk=pk).delete()

            if file_type == AUDIO_FILE_TYPE[1]:
                Podcast.objects.get(pk=pk).delete()

            if file_type == AUDIO_FILE_TYPE[2]:
                Audiobook.objects.get(pk=pk).delete()

            message = "Audio file deleted Successfully!"
            return Response({
                        'status' : True,
                        'message' : message,
                        'data': {}

                    }, status=status.HTTP_200_OK)
        except Exception as inst:
            message = str(inst)
            return Response({
                    'status' : False,
                    'message': message
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, file_type, pk):
        try:
            if file_type not in AUDIO_FILE_TYPE:
                message = f"Invalid file type- {file_type}! Select from {AUDIO_FILE_TYPE}"
                return Response({
                            'status' : False,
                            'message': message
                        }, status=status.HTTP_404_NOT_FOUND)

            if file_type == AUDIO_FILE_TYPE[0]:
                song = Song.objects.get(pk=pk)
                serializer = SongSerializer(song, data=request.data['audioFileMetadata'], partial=True, context={"request": request})

            if file_type == AUDIO_FILE_TYPE[1]:
                podcast = Podcast.objects.get(pk=pk)
                serializer = PodcastSerializer(podcast, data=request.data['audioFileMetadata'], partial=True, context={"request": request})

            if file_type == AUDIO_FILE_TYPE[2]:
                audiobook = Audiobook.objects.get(pk=pk)
                serializer = AudiobookSerializer(audiobook, data=request.data['audioFileMetadata'], partial=True, context={"request": request})

            message = "Audio file updated successfully!"
            response_status, result, message = serialized_response(serializer, message)
            status_code = status.HTTP_200_OK if response_status else status.HTTP_400_BAD_REQUEST
            
            return Response({
                    'status' : True,
                    'message': message,
                    'data': result
                }, status=status_code)

        except Exception as inst:
            message = str(inst)
            return Response({
                    'status' : False,
                    'message': message
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)