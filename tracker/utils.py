from django.utils import timezone
from .models import LogEntry
from datetime import timedelta

def has_logged_today(habit):
    today = timezone.now().date()
    return LogEntry.objects.filter(habit=habit, date=today).exists()


def get_today_log(habit):
    today = timezone.now().date()
    return LogEntry.objects.filter(habit=habit, date=today).first()


def calculate_streak(habit):
    today = timezone.now().date()
    streak = 0
    current_date = today

    # Walk backwards day by day
    while LogEntry.objects.filter(habit=habit, date=current_date).exists():
        streak += 1
        current_date -= timedelta(days=1)

    return streak