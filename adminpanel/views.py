from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render
from habits.models import Habit, HabitLog

@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard(request):
    # System-level stats
    total_users = User.objects.count()
    total_habits = Habit.objects.count()
    total_logs = HabitLog.objects.count()

    avg_habits = round(total_habits / total_users, 2) if total_users > 0 else 0

    # User-level stats
    users = User.objects.annotate(
        habit_count=Count('habit', distinct=True),
        log_count=Count('habitlog', distinct=True)
    ).order_by('username')

    context = {
        "total_users": total_users,
        "total_habits": total_habits,
        "total_logs": total_logs,
        "avg_habits": avg_habits,
        "users": users,
    }

    return render(request, "admin_dashboard.html", context)
