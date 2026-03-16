from django.test import TestCase
from django.contrib.auth.models import User
from tracker.models import Habit, LogEntry
from accounts.models import Profile
from datetime import date

class ProfileModelTests(TestCase):
    def test_profile_created_on_user_creation(self):
        user = User.objects.create_user(username="testuser", password="pass123")
        self.assertTrue(Profile.objects.filter(user=user).exists())

    def test_profile_role_default(self):
        user = User.objects.create_user(username="roleuser", password="pass123")
        profile = Profile.objects.get(user=user)
        self.assertEqual(profile.role, "user")


class HabitModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="habituser", password="pass123")

    def test_habit_string_representation(self):
        habit = Habit.objects.create(
            user=self.user,
            name="Drink Water",
            description="Stay hydrated",
            habit_type="positive"
        )
        self.assertEqual(str(habit), "Drink Water (habituser)")

    def test_unique_habit_name_per_user(self):
        Habit.objects.create(
            user=self.user,
            name="Read",
            description="Read daily",
            habit_type="positive"
        )
        with self.assertRaises(Exception):
            Habit.objects.create(
                user=self.user,
                name="Read",
                description="Duplicate",
                habit_type="positive"
            )


class LogEntryModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="loguser", password="pass123")
        self.habit = Habit.objects.create(
            user=self.user,
            name="Exercise",
            description="Daily workout",
            habit_type="positive"
        )

    def test_logentry_string_representation(self):
        log = LogEntry.objects.create(
            habit=self.habit,
            date=date.today(),
            completed=True
        )
        self.assertIn("Exercise", str(log))

    def test_unique_log_per_day(self):
        LogEntry.objects.create(
            habit=self.habit,
            date=date.today(),
            completed=True
        )
        with self.assertRaises(Exception):
            LogEntry.objects.create(
                habit=self.habit,
                date=date.today(),
                completed=False
            )
