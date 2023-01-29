from rest_framework import serializers

from meeting.models import Meeting, Topic


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ("title","created_by","created_at","updated_at")

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ("title","created_by","created_at","updated_at","problem","resolution","meeting")
