from django.db import models
from django.contrib.auth.models import User


class Habit(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="habits"
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    habit_type = models.CharField(max_length=10, choices=[('positive', 'Positive'), ('negative', 'Negative')], default='positive')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "name"],
                name="unique_habit_name_per_user"
            )
        ]
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.name} ({self.user.username})"


class LogEntry(models.Model):
    habit = models.ForeignKey(
        Habit,
        on_delete=models.CASCADE,
        related_name="logs"
    )
    date = models.DateField()
    completed = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["habit", "date"],
                name="unique_log_per_habit_per_date"
            )
        ]
        ordering = ["-date"]

    def __str__(self):
        return f"{self.habit.name} on {self.date} — {'Done' if self.completed else 'Not done'}"


class LogEntry(models.Model):
    habit = models.ForeignKey(
        Habit,
        on_delete=models.CASCADE,
        related_name="logs"
    )
    date = models.DateField()
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-date"]
        unique_together = ("habit", "date")

    def __str__(self):
        return f"{self.habit.name} — {self.date}"
