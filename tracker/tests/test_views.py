from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from tracker.models import Habit

class ViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="viewuser", password="pass123")
        self.admin = User.objects.create_superuser(username="admin", password="adminpass")
        self.client.login(username="viewuser", password="pass123")

    def test_dashboard_requires_login(self):
        self.client.logout()
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 302)
        self.assertIn("/login", response.url)

    def test_habit_list_view(self):
        response = self.client.get(reverse("habit_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "habit_list.html")

    def test_habit_detail_view(self):
        habit = Habit.objects.create(
            user=self.user,
            name="Test Habit",
            description="Test",
            habit_type="positive"
        )
        response = self.client.get(reverse("habit_detail", args=[habit.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Habit")

    def test_admin_dashboard_superuser_only(self):
        self.client.login(username="viewuser", password="pass123")
        response = self.client.get("/admin-dashboard/")
        self.assertEqual(response.status_code, 302)

        self.client.login(username="admin", password="adminpass")
        response = self.client.get("/admin-dashboard/")
        self.assertEqual(response.status_code, 200)
