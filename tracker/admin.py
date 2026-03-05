from django.contrib import admin
from .models import Habit, LogEntry


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "is_active", "created_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("name", "user__username")


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ("habit", "date", "completed", "created_at")
    list_filter = ("completed", "date")
    search_fields = ("habit__name",)