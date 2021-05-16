from django.db.models.fields import CharField, PositiveIntegerField
from rest_framework import serializers
from .models import Song, Audiobook, Podcast, PodcastParticipant


class SongSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, max_length=100)
    duration = serializers.IntegerField(required=True, min_value=0)

    class Meta:
        model = Song
        fields = ('pk', 'name', 'duration', 'uploaded_time')


class PodcastParticipantSerializer(serializers.Serializer):
    participant = serializers.CharField(required=False, max_length=100)


class PodcastSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, max_length=100)
    duration = serializers.IntegerField(required=True, min_value=0)
    host = serializers.CharField(required=True, max_length=100)
    participants = serializers.ListField(required=False)

    class Meta:
        model = Podcast
        fields = ('pk', 'name', 'duration', 'uploaded_time', 'host', 'participants')

    def create(self, validated_data):
        participants = validated_data.pop('participants', None)
        if participants:
            if len(participants) > 10:
                raise serializers.ValidationError("Only 10 participants are allowed in Podcast")
            serializer = PodcastParticipantSerializer(participants, many=True)
            podcast = Podcast(**validated_data)
            podcast.save()
            for participant in participants:
                PodcastParticipant.objects.create(podcast=podcast, participant=participant)
        return validated_data

    def update(self, instance, validated_data):
        participants = validated_data.pop('participants', None)
        super().update(instance, validated_data)
        if participants:
            PodcastParticipant.objects.filter(podcast=instance).delete()
            if len(participants) > 10:
                raise serializers.ValidationError("Only 10 participants are allowed in Podcast")
            serializer = PodcastParticipantSerializer(participants, many=True)
            for participant in participants:
                PodcastParticipant.objects.create(podcast=instance, participant=participant)
        return validated_data


class AudiobookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True, max_length=100)
    author = serializers.CharField(required=True, max_length=100)
    narrator = serializers.CharField(required=True, max_length=100)
    duration = serializers.IntegerField(required=True, min_value=0)

    class Meta:
        model = Audiobook
        fields = ('pk', 'title', 'author', 'narrator', 'duration', 'uploaded_time')


class PodcastDetailSerializer(serializers.ModelSerializer):
    participants = serializers.SerializerMethodField()

    class Meta:
        model = Podcast
        fields = ('pk', 'name', 'duration', 'uploaded_time', 'host', 'participants')

    def get_participants(self, podcast):
        participants = PodcastParticipant.objects.filter(podcast=podcast)
        return PodcastParticipantSerializer(participants, many=True).data