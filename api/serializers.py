from rest_framework import serializers

from meeting.models import Meeting, Topic

class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = ["title","created_at","updated_at","problem","resolution"]

class MeetingSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.username', read_only=True)
    topic = TopicSerializer(source='Meeting', many=True, read_only=True)
    class Meta:
        model = Meeting
        fields = ["title","created_by","created_at","updated_at","topic"]


