from django.urls import path

from .views import MeetingAPIView

urlpatterns = [
    path("", MeetingAPIView.as_view(), name = "meeting_list"),
]