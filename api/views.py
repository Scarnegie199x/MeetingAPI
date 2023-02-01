from django.shortcuts import render
from rest_framework import generics

from meeting.models import Meeting, Topic
from .serializers import MeetingSerializer, TopicSerializer

class MeetingAPIView(generics.ListAPIView):
    queryset=Meeting.objects.all()
    serializer_class = MeetingSerializer

class TopicAPIView(generics.ListAPIView):
    queryset=Topic.objects.all()
    serializer_class = TopicSerializer

# Create your views here.
