from django.test import SimpleTestCase
from django.urls import reverse, resolve
from tracker import views

class URLTests(SimpleTestCase):
    def test_habit_list_url_resolves(self):
        url = reverse("habit_list")
        self.assertEqual(resolve(url).func.view_class, views.HabitListView)

    def test_dashboard_url_resolves(self):
        url = reverse("dashboard")
        self.assertEqual(resolve(url).func, views.dashboard)
