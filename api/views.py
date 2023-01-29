from django.shortcuts import render
from rest_framework import generics

from meeting.models import Meeting, Topic
from .serializers import MeetingSerializer

class MeetingAPIView(generics.ListAPIView):
    queryset=Meeting.objects.all()
    #queryset2=Topic.objects.all()
    serializer_class = MeetingSerializer

# Create your views here.
