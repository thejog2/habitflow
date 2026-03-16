from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from tracker.models import Habit

class PermissionTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="u1", password="pass123")
        self.user2 = User.objects.create_user(username="u2", password="pass123")

        self.habit = Habit.objects.create(
            user=self.user1,
            name="Private Habit",
            description="Test",
            habit_type="positive"
        )

    def test_user_cannot_access_another_users_habit(self):
        self.client.login(username="u2", password="pass123")
        response = self.client.get(reverse("habit_detail", args=[self.habit.id]))
        self.assertEqual(response.status_code, 404)
