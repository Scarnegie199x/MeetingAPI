from django.urls import path

from .views import MeetingAPIView,TopicAPIView

urlpatterns = [
    path("meeting/", MeetingAPIView.as_view(), name = "meeting_list"),
    path("topic/", TopicAPIView.as_view(), name = "meeting_list"),
]