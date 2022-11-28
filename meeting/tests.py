from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Meeting, Topic


class MeetingTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="testuser@email.com",
            password="testpass123"
        )

        cls.meeting = Meeting.objects.create(
            title="Test Meeting for Python",
            created_by = cls.user
        )

        cls.topic = Topic.objects.create(
            meeting = cls.meeting,
            title = "Python and testing issues",
            problem = "Test framework is too efficent",
            resolution = "Run more tests",
        )

    def test_meeting(self):
        self.assertEqual(f"{self.meeting.title}", "Test Meeting for Python")
        self.assertEqual(f"{self.meeting.created_by}", "testuser")

    def test_topic(self):
        self.assertEqual(f"{self.topic.title}", "Python and testing issues")
        self.assertEqual(f"{self.topic.problem}", "Test framework is too efficent")
        self.assertEqual(f"{self.topic.resolution}", "Run more tests")
